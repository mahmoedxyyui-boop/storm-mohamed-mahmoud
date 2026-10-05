/**
 * محمد محمود ذهب ستور | MOHAMED MAHMOUD DAHAB STORE
 * Advanced E-Commerce Logic:
 * - Gold in Black Theme
 * - Live Dual-Color Switcher
 * - Shopping Cart & Drawer
 * - Electronic Invoice Generation
 * - Direct WhatsApp Checkout to 01126618186
 */

// Application State
const appState = {
  activeCategory: 'all',
  searchQuery: '',
  sortBy: 'featured',
  activeColors: {}, // productId -> 'dual' | 'c1' | 'c2'
  cart: JSON.parse(localStorage.getItem('dahab_cart') || '[]'),
  currentInvoiceNum: null
};

// Target WhatsApp for Orders & Invoices
const INVOICE_TARGET_WHATSAPP = '201126618186'; // 01126618186

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  initHeroCarousel();
  renderProducts();
  setupListeners();
  updateCartBadge();
  renderCartDrawer();
});

// Format Price
function formatPrice(num) {
  return Number(num).toLocaleString('ar-EG');
}

// Save Cart to LocalStorage
function saveCart() {
  localStorage.setItem('dahab_cart', JSON.stringify(appState.cart));
  updateCartBadge();
  renderCartDrawer();
}

// Update Cart Count Badge
function updateCartBadge() {
  const count = appState.cart.reduce((sum, item) => sum + item.qty, 0);
  const badges = document.querySelectorAll('.cart-count-badge');
  badges.forEach(b => {
    b.textContent = count;
    b.style.display = count > 0 ? 'inline-block' : 'none';
  });
}

// Generate Invoice Number
function generateInvoiceNumber() {
  if (!appState.currentInvoiceNum) {
    const rand = Math.floor(1000 + Math.random() * 9000);
    appState.currentInvoiceNum = `DHB-${rand}`;
  }
  return appState.currentInvoiceNum;
}

// Add Item to Cart
function addToCart(productId, chosenColorName = null, chosenColorHex = null) {
  const product = getProductById(productId);
  if (!product) return;

  const activeColorKey = appState.activeColors[productId] || 'dual';
  
  let finalColorName = chosenColorName;
  let finalColorHex = chosenColorHex;
  let finalImg = product.dualImg || product.img;

  if (!finalColorName) {
    if (activeColorKey === 'c1' && product.color1) {
      finalColorName = product.color1.name;
      finalColorHex = product.color1.hex;
      finalImg = product.color1.img;
    } else if (activeColorKey === 'c2' && product.color2) {
      finalColorName = product.color2.name;
      finalColorHex = product.color2.hex;
      finalImg = product.color2.img;
    } else if (product.color1) {
      finalColorName = `اللونين معاً (${product.color1.name.split(' ')[0]} / ${product.color2.name.split(' ')[0]})`;
      finalColorHex = product.color1.hex;
    } else {
      finalColorName = 'اللون القياسي';
    }
  }

  // Check if identical product + color already in cart
  const existingIndex = appState.cart.findIndex(
    item => item.id === product.id && item.colorName === finalColorName
  );

  if (existingIndex > -1) {
    appState.cart[existingIndex].qty += 1;
  } else {
    appState.cart.push({
      id: product.id,
      name: product.fullName || product.name,
      brand: product.brand,
      price: product.price,
      colorName: finalColorName,
      colorHex: finalColorHex,
      img: finalImg,
      qty: 1
    });
  }

  saveCart();
  showToast(`تمت إضافة ${product.name} إلى السلة بنجاح! 🛒`);
  openCartDrawer();
}

// Buy Now (Fast Checkout)
function buyNow(productId) {
  addToCart(productId);
  openCheckoutModal();
}

// Update Cart Quantity
function updateCartQty(index, delta) {
  if (appState.cart[index]) {
    appState.cart[index].qty += delta;
    if (appState.cart[index].qty <= 0) {
      appState.cart.splice(index, 1);
    }
    saveCart();
  }
}

// Remove from Cart
function removeCartItem(index) {
  if (appState.cart[index]) {
    appState.cart.splice(index, 1);
    saveCart();
  }
}

// Calculate Cart Total
function getCartTotal() {
  return appState.cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
}

// Render Cart Drawer
function renderCartDrawer() {
  const container = document.getElementById('cart-items-container');
  const totalElem = document.getElementById('cart-total-value');
  const footerElem = document.getElementById('cart-drawer-footer');
  
  if (!container) return;

  if (appState.cart.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 60px 20px; color: var(--text-muted);">
        <i class="fa-solid fa-cart-shopping" style="font-size: 3rem; color: var(--gold-border); margin-bottom: 14px; display: block;"></i>
        <h4 style="color: #ffffff; font-size: 1.15rem; margin-bottom: 6px;">السلة فارغة حالياً</h4>
        <p style="font-size: 0.85rem; margin-bottom: 20px;">تصفح أحدث هواتف OPPO و realme وأضف ما يعجبك!</p>
        <button onclick="closeCartDrawer()" class="tab-pill-btn active" style="padding: 9px 22px;">تصفح الهواتف الآن</button>
      </div>
    `;
    if (totalElem) totalElem.textContent = '0 ج.م';
    if (footerElem) footerElem.style.display = 'none';
    return;
  }

  if (footerElem) footerElem.style.display = 'block';

  container.innerHTML = appState.cart.map((item, idx) => `
    <div class="cart-item-card">
      <img src="${item.img}" alt="${item.name}" class="cart-item-thumbnail">
      <div class="cart-item-info">
        <h4 class="cart-item-name" title="${item.name}">${item.name}</h4>
        <div class="cart-item-chosen-color">
          ${item.colorHex ? `<span class="swatch-circle" style="width: 12px; height: 12px; background: ${item.colorHex};"></span>` : ''}
          <span>${item.colorName}</span>
        </div>
        <div class="cart-item-price">${formatPrice(item.price)} ج.م</div>
      </div>
      <div class="cart-item-qty-controls">
        <button type="button" class="qty-btn" onclick="updateCartQty(${idx}, 1)">+</button>
        <span style="font-weight: 800; font-size: 0.9rem; min-width: 16px; text-align: center;">${item.qty}</span>
        <button type="button" class="qty-btn" onclick="updateCartQty(${idx}, -1)">-</button>
      </div>
      <button type="button" class="cart-item-remove-btn" onclick="removeCartItem(${idx})" title="حذف">
        <i class="fa-solid fa-trash-can"></i>
      </button>
    </div>
  `).join('');

  if (totalElem) {
    totalElem.textContent = `${formatPrice(getCartTotal())} ج.م`;
  }
}

// Open / Close Cart Drawer
function openCartDrawer() {
  const drawer = document.getElementById('cart-drawer-overlay');
  if (drawer) drawer.classList.add('active');
}

function closeCartDrawer() {
  const drawer = document.getElementById('cart-drawer-overlay');
  if (drawer) drawer.classList.remove('active');
}

// Switch Mobile Color on Card
function switchMobileColor(productId, colorType) {
  appState.activeColors[productId] = colorType;
  
  const card = document.getElementById(`mobile-card-${productId}`);
  if (!card) return;
  
  const product = getProductById(productId);
  if (!product) return;
  
  const imgElem = card.querySelector('.card-visual-img');
  const colorBtns = card.querySelectorAll('.color-switch-btn, .btn-dual-both');
  
  colorBtns.forEach(btn => btn.classList.remove('active'));
  
  let targetImg = product.dualImg || product.img;
  
  if (colorType === 'c1' && product.color1) {
    targetImg = product.color1.img;
    const c1Btn = card.querySelector('[data-type="c1"]');
    if (c1Btn) c1Btn.classList.add('active');
  } else if (colorType === 'c2' && product.color2) {
    targetImg = product.color2.img;
    const c2Btn = card.querySelector('[data-type="c2"]');
    if (c2Btn) c2Btn.classList.add('active');
  } else {
    targetImg = product.dualImg || product.img;
    const dualBtn = card.querySelector('[data-type="dual"]');
    if (dualBtn) dualBtn.classList.add('active');
  }
  
  imgElem.style.opacity = '0';
  setTimeout(() => {
    imgElem.src = targetImg;
    imgElem.style.opacity = '1';
  }, 120);
}

// Render Products Grid
function renderProducts() {
  const grid = document.getElementById('products-grid');
  if (!grid) return;
  
  let list = [...PRODUCTS_DATA];
  
  if (appState.activeCategory !== 'all') {
    list = list.filter(p => p.category === appState.activeCategory);
  }
  
  if (appState.searchQuery.trim() !== '') {
    const q = appState.searchQuery.toLowerCase().trim();
    list = list.filter(p => {
      return (
        p.name.toLowerCase().includes(q) ||
        p.fullName.toLowerCase().includes(q) ||
        p.brand.toLowerCase().includes(q) ||
        (p.rom && p.rom.toLowerCase().includes(q)) ||
        (p.specs && p.specs.some(s => s.toLowerCase().includes(q))) ||
        (p.color1 && p.color1.name.toLowerCase().includes(q)) ||
        (p.color2 && p.color2.name.toLowerCase().includes(q))
      );
    });
  }
  
  if (appState.sortBy === 'price-asc') {
    list.sort((a, b) => a.price - b.price);
  } else if (appState.sortBy === 'price-desc') {
    list.sort((a, b) => b.price - a.price);
  } else if (appState.sortBy === 'name') {
    list.sort((a, b) => a.name.localeCompare(b.name, 'ar'));
  }
  
  if (list.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 50px 20px; background: #0c111e; border-radius: 20px; border: 1.5px dashed var(--gold-border);">
        <h3 style="color: #ffffff; font-size: 1.3rem; margin-bottom: 8px;">لم نجد أجهزة مطابقة لبحثك</h3>
        <p style="color: var(--text-muted); margin-bottom: 16px;">جرب تغيير كلمة البحث أو الضغط على جميع الموديلات</p>
        <button onclick="resetSearchFilters()" class="tab-pill-btn active" style="padding: 10px 24px;">عرض جميع هواتف OPPO و realme</button>
      </div>
    `;
    return;
  }
  
  grid.innerHTML = list.map(item => {
    const isMobile = item.category === 'oppo' || item.category === 'realme';
    const activeColorState = appState.activeColors[item.id] || 'dual';
    
    let displayImg = item.dualImg || item.img;
    if (activeColorState === 'c1' && item.color1) displayImg = item.color1.img;
    if (activeColorState === 'c2' && item.color2) displayImg = item.color2.img;

    const brandClass = item.brand.toLowerCase() === 'oppo' ? 'oppo' : 'realme';

    let colorsHtml = '';
    if (isMobile && item.color1 && item.color2) {
      colorsHtml = `
        <div class="card-colors-panel">
          <div class="colors-panel-label">
            <span>اللونين الرسميين:</span>
            <strong>معاينة تفاعلية</strong>
          </div>
          <div class="colors-buttons-grid">
            <button type="button" class="color-switch-btn ${activeColorState === 'c1' ? 'active' : ''}" data-type="c1" onclick="switchMobileColor('${item.id}', 'c1')" title="${item.color1.name}">
              <span class="swatch-circle" style="background: ${item.color1.hex};"></span>
              <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${item.color1.name.split(' ')[0]}</span>
            </button>
            <button type="button" class="color-switch-btn ${activeColorState === 'c2' ? 'active' : ''}" data-type="c2" onclick="switchMobileColor('${item.id}', 'c2')" title="${item.color2.name}">
              <span class="swatch-circle" style="background: ${item.color2.hex};"></span>
              <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${item.color2.name.split(' ')[0]}</span>
            </button>
            <button type="button" class="btn-dual-both ${activeColorState === 'dual' ? 'active' : ''}" data-type="dual" onclick="switchMobileColor('${item.id}', 'dual')">
              معاً
            </button>
          </div>
        </div>
      `;
    }

    let specsHtml = '';
    if (item.ram && item.rom) {
      specsHtml = `
        <div class="card-specs-row">
          <span class="spec-badge gold">RAM: ${item.ram}</span>
          <span class="spec-badge gold">ROM: ${item.rom}</span>
          ${item.network ? `<span class="spec-badge">${item.network}</span>` : ''}
        </div>
      `;
    } else {
      specsHtml = `
        <div class="card-specs-row">
          <span class="spec-badge gold">إكسسوار أصلي</span>
          <span class="spec-badge">ضمان معتمد</span>
        </div>
      `;
    }

    return `
      <div class="mobile-card" id="mobile-card-${item.id}">
        <div class="card-header-tags">
          <span class="brand-badge ${brandClass}">${item.brand}</span>
          ${item.badge ? `<span class="feature-tag">${item.badge}</span>` : ''}
        </div>

        <div class="card-visual-frame" onclick="openDetailsModal('${item.id}')">
          <img src="${displayImg}" alt="${item.fullName}" class="card-visual-img" loading="lazy">
        </div>

        ${colorsHtml}

        <h3 class="card-device-name" onclick="openDetailsModal('${item.id}')">
          ${item.fullName || item.name}
        </h3>

        ${specsHtml}

        <div class="card-price-bottom">
          <div class="price-title-label">
            السعر الرسمي:
          </div>
          <div class="price-amount-wrap">
            <span class="price-numerical-value">${formatPrice(item.price)}</span>
            <span class="price-unit">ج.م</span>
          </div>
        </div>

        <!-- 3-Button Shopping System -->
        <div class="card-ecommerce-actions">
          <button type="button" class="btn-card-add-cart" onclick="addToCart('${item.id}')">
            <i class="fa-solid fa-cart-plus"></i>
            <span>أضف للسلة</span>
          </button>
          <button type="button" class="btn-card-buy-instant" onclick="buyNow('${item.id}')">
            <i class="fa-solid fa-bolt"></i>
            <span>شراء فوري</span>
          </button>
        </div>

        <button type="button" class="btn-card-details-full" onclick="openDetailsModal('${item.id}')">
          <i class="fa-solid fa-circle-info"></i>
          <span>عرض المواصفات الكاملة</span>
        </button>
      </div>
    `;
  }).join('');
}

// Reset Search
function resetSearchFilters() {
  appState.activeCategory = 'all';
  appState.searchQuery = '';
  
  const searchInput = document.getElementById('search-input');
  if (searchInput) searchInput.value = '';
  
  document.querySelectorAll('.tab-pill-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.category === 'all');
  });
  
  renderProducts();
}

// Setup Event Listeners
function setupListeners() {
  document.querySelectorAll('.tab-pill-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tab-pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      appState.activeCategory = btn.dataset.category;
      renderProducts();
    });
  });

  const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      appState.searchQuery = e.target.value;
      renderProducts();
    });
  }

  const sortSelect = document.getElementById('sort-select');
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      appState.sortBy = e.target.value;
      renderProducts();
    });
  }

  // Backdrop clicks
  const cartOverlay = document.getElementById('cart-drawer-overlay');
  if (cartOverlay) {
    cartOverlay.addEventListener('click', (e) => {
      if (e.target === cartOverlay) closeCartDrawer();
    });
  }

  const invoiceOverlay = document.getElementById('invoice-modal-overlay');
  if (invoiceOverlay) {
    invoiceOverlay.addEventListener('click', (e) => {
      if (e.target === invoiceOverlay) closeCheckoutModal();
    });
  }

  const deviceModal = document.getElementById('device-modal');
  if (deviceModal) {
    deviceModal.addEventListener('click', (e) => {
      if (e.target === deviceModal) closeDetailsModal();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeCartDrawer();
      closeCheckoutModal();
      closeDetailsModal();
    }
  });
}

// Hero Carousel
function initHeroCarousel() {
  const imgElem = document.getElementById('hero-flagship-img');
  const titleElem = document.getElementById('hero-flagship-title');
  const priceElem = document.getElementById('hero-flagship-price');
  
  if (!imgElem) return;
  
  const showcaseItems = [
    getProductById('oppo_reno_16_5g'),
    getProductById('realme_16_pro_plus_5g'),
    getProductById('oppo_reno_15_256'),
    getProductById('realme_16_pro_5g'),
    getProductById('oppo_reno_16f_12')
  ].filter(Boolean);
  
  let idx = 0;
  setInterval(() => {
    idx = (idx + 1) % showcaseItems.length;
    const phone = showcaseItems[idx];
    
    imgElem.style.opacity = '0';
    setTimeout(() => {
      imgElem.src = phone.dualImg;
      titleElem.textContent = phone.fullName;
      priceElem.textContent = `${formatPrice(phone.price)} ج.م`;
      imgElem.style.opacity = '1';
    }, 200);
  }, 4000);
}

// ==========================================================================
// CHECKOUT & INVOICE GENERATOR (TARGET: 01126618186)
// ==========================================================================
function openCheckoutModal() {
  if (appState.cart.length === 0) {
    showToast('برجاء إضافة منتج إلى السلة أولاً!');
    return;
  }

  closeCartDrawer();
  const modal = document.getElementById('invoice-modal-overlay');
  const body = document.getElementById('invoice-modal-body');
  if (!modal || !body) return;

  const invoiceNum = generateInvoiceNumber();
  const dateStr = new Date().toLocaleDateString('ar-EG', { year: 'numeric', month: 'long', day: 'numeric' });
  const total = getCartTotal();

  body.innerHTML = `
    <div class="invoice-paper-frame">
      <!-- Store & Invoice Header -->
      <div class="invoice-header-branding">
        <div style="display: flex; align-items: center; gap: 12px;">
          <img src="assets/images/brand/dahab_logo.jpg" alt="محمد محمود ذهب ستور" style="width: 50px; height: 50px; border-radius: 50%; border: 2px solid var(--gold-primary);">
          <div class="invoice-store-info">
            <h3>محمد محمود ذهب ستور</h3>
            <p>فاتورة شراء وتأكيد طلب إلكترونية معتمدة</p>
          </div>
        </div>
        <div class="invoice-number-tag">
          <div style="font-size: 0.75rem; color: var(--text-muted);">رقم الفاتورة:</div>
          <div class="inv-num">#${invoiceNum}</div>
          <div style="font-size: 0.75rem; color: var(--gold-light);">${dateStr}</div>
        </div>
      </div>

      <!-- Customer Details Form -->
      <h4 style="font-size: 1rem; color: var(--gold-light); margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
        <i class="fa-solid fa-user-pen"></i>
        بيانات العميل والتوصيل:
      </h4>

      <div class="invoice-form-grid">
        <div class="form-group-field">
          <label class="form-label">الاسم بالكامل <span style="color: #ef4444;">*</span>:</label>
          <input type="text" id="cust-name" class="form-input" placeholder="اكتب اسمك ثلاثياً..." required>
        </div>

        <div class="form-group-field">
          <label class="form-label">رقم الهاتف للتواصل <span style="color: #ef4444;">*</span>:</label>
          <input type="tel" id="cust-phone" class="form-input" placeholder="مثال: 010... أو 011..." required>
        </div>

        <div class="form-group-field full-width">
          <label class="form-label">المحافظة والعنوان بالتفصيل <span style="color: #ef4444;">*</span>:</label>
          <input type="text" id="cust-address" class="form-input" placeholder="المحافظة - المركز / المنطقة - اسم الشارع والعمارة..." required>
        </div>

        <div class="form-group-field">
          <label class="form-label">طريقة الدفع المفضلة:</label>
          <select id="cust-payment" class="form-input">
            <option value="الدفع كاش عند الاستلام">الدفع كاش عند الاستلام بعد المعاينة</option>
            <option value="إنستاباي (InstaPay)">تحويل عبر إنستاباي (InstaPay)</option>
            <option value="محفظة فودافون كاش / إلكترونية">محفظة إلكترونية (فودافون كاش / اتصالات)</option>
            <option value="تقسيط (أمان / فرصة / فاليو / فيزا)">تقسيط (أمان / فرصة / فاليو / فيزا)</option>
          </select>
        </div>

        <div class="form-group-field">
          <label class="form-label">ملاحظات إضافية (اختياري):</label>
          <input type="text" id="cust-notes" class="form-input" placeholder="ميعاد مفضل للاستلام، استفسار...">
        </div>
      </div>

      <!-- Items Table -->
      <h4 style="font-size: 1rem; color: var(--gold-light); margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
        <i class="fa-solid fa-boxes-stacked"></i>
        المنتجات المحجوزة بالفاتورة:
      </h4>

      <table class="invoice-items-table">
        <thead>
          <tr>
            <th>المنتج / الجهاز</th>
            <th>اللون المختار</th>
            <th style="text-align: center;">الكمية</th>
            <th>السعر</th>
            <th>الإجمالي</th>
          </tr>
        </thead>
        <tbody>
          ${appState.cart.map(item => `
            <tr>
              <td>
                <strong>${item.name}</strong>
              </td>
              <td>
                <span style="color: var(--gold-light); font-weight: 700;">${item.colorName}</span>
              </td>
              <td style="text-align: center; font-weight: 800;">${item.qty}</td>
              <td>${formatPrice(item.price)} ج.م</td>
              <td style="font-weight: 900; color: var(--gold-light);">${formatPrice(item.price * item.qty)} ج.م</td>
            </tr>
          `).join('')}
        </tbody>
      </table>

      <!-- Total Row -->
      <div class="invoice-total-highlight">
        <span style="font-size: 1.15rem; font-weight: 900; color: #ffffff;">إجمالي الفاتورة المطلوب سدادها:</span>
        <span style="font-size: 1.85rem; font-weight: 900; color: var(--gold-light);">${formatPrice(total)} ج.م</span>
      </div>

      <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 10px; display: flex; align-items: center; gap: 6px;">
        <i class="fa-solid fa-circle-check" style="color: var(--gold-primary);"></i>
        ضمان محلي معتمد • فحص ومعاينة الشحنة قبل الدفع • سيتم إرسال الفاتورة تلقائياً لإدارة المعرض.
      </div>
    </div>

    <!-- Submit to WhatsApp Button (01126618186) -->
    <button type="button" class="btn-send-whatsapp-invoice" onclick="sendInvoiceWhatsApp()">
      <i class="fa-brands fa-whatsapp" style="font-size: 1.5rem;"></i>
      <span>تأكيد الطلب وإرسال الفاتورة عبر واتساب (01126618186)</span>
    </button>
  `;

  modal.classList.add('active');
}

function closeCheckoutModal() {
  const modal = document.getElementById('invoice-modal-overlay');
  if (modal) modal.classList.remove('active');
}

// Send Invoice to WhatsApp (01126618186)
function sendInvoiceWhatsApp() {
  const nameInput = document.getElementById('cust-name');
  const phoneInput = document.getElementById('cust-phone');
  const addrInput = document.getElementById('cust-address');
  const payInput = document.getElementById('cust-payment');
  const notesInput = document.getElementById('cust-notes');

  const name = nameInput ? nameInput.value.trim() : '';
  const phone = phoneInput ? phoneInput.value.trim() : '';
  const address = addrInput ? addrInput.value.trim() : '';
  const payment = payInput ? payInput.value : 'الدفع كاش عند الاستلام';
  const notes = notesInput ? notesInput.value.trim() : 'لا توجد';

  if (!name || !phone || !address) {
    alert('برجاء كتابة الاسم، ورقم الهاتف، والعنوان بالتفصيل لإتمام الفاتورة!');
    if (!name && nameInput) nameInput.focus();
    else if (!phone && phoneInput) phoneInput.focus();
    else if (!address && addrInput) addrInput.focus();
    return;
  }

  const invoiceNum = generateInvoiceNumber();
  const now = new Date();
  const dateStr = now.toLocaleDateString('ar-EG');
  const timeStr = now.toLocaleTimeString('ar-EG', { hour: '2-digit', minute: '2-digit' });
  const total = getCartTotal();

  let msg = `🌟 *فاتورة طلب جديدة - محمد محمود ذهب ستور* 🌟\n`;
  msg += `==============================\n`;
  msg += `📋 *رقم الفاتورة:* #${invoiceNum}\n`;
  msg += `📅 *التاريخ:* ${dateStr} (${timeStr})\n\n`;
  msg += `👤 *بيانات العميل:* \n`;
  msg += `• *الاسم:* ${name}\n`;
  msg += `• *الموبايل:* ${phone}\n`;
  msg += `• *العنوان والمحافظة:* ${address}\n`;
  msg += `• *طريقة الدفع:* ${payment}\n`;
  if (notes && notes !== 'لا توجد') {
    msg += `• *ملاحظات العميل:* ${notes}\n`;
  }
  msg += `==============================\n`;
  msg += `📦 *المنتجات المطلوبة:* \n\n`;

  appState.cart.forEach((item, i) => {
    msg += `${i + 1}) *${item.name}*\n`;
    msg += `   🎨 اللون: *${item.colorName}*\n`;
    msg += `   🔢 الكمية: ${item.qty} × ${item.price.toLocaleString('en-US')} ج.م = *${(item.price * item.qty).toLocaleString('en-US')} ج.م*\n\n`;
  });

  msg += `------------------------------\n`;
  msg += `💰 *إجمالي الفاتورة المطلوب سدادها:* *${total.toLocaleString('en-US')} ج.م*\n`;
  msg += `==============================\n`;
  msg += `🚚 برجاء تأكيد ميعاد التوصيل والشحن. شكراً لكم!\n`;

  const waUrl = `https://wa.me/${INVOICE_TARGET_WHATSAPP}?text=${encodeURIComponent(msg)}`;

  // Clear Cart after submission
  appState.cart = [];
  appState.currentInvoiceNum = null;
  saveCart();
  closeCheckoutModal();

  showToast('تم تجهيز الفاتورة وجاري فتح الواتساب لإرسالها للرقم 01126618186... 🎉');

  // Open WhatsApp
  window.open(waUrl, '_blank');
}

// Open Details Modal
function openDetailsModal(productId) {
  const item = getProductById(productId);
  if (!item) return;
  
  const modal = document.getElementById('device-modal');
  const body = document.getElementById('modal-card-body');
  if (!modal || !body) return;
  
  const isMobile = item.category === 'oppo' || item.category === 'realme';
  const activeColor = appState.activeColors[productId] || 'dual';
  
  let currentImg = item.dualImg || item.img;
  if (activeColor === 'c1' && item.color1) currentImg = item.color1.img;
  if (activeColor === 'c2' && item.color2) currentImg = item.color2.img;

  let colorSwitchModalHtml = '';
  if (isMobile && item.color1 && item.color2) {
    colorSwitchModalHtml = `
      <div style="background: rgba(212, 175, 55, 0.08); border: 1.5px solid var(--gold-border); border-radius: 12px; padding: 14px; margin: 16px 0;">
        <h4 style="font-size: 0.92rem; color: var(--gold-light); margin-bottom: 10px;">الألوان الرسمية المعتمدة للجهاز:</h4>
        <div style="display: flex; flex-direction: column; gap: 8px;">
          <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(0,0,0,0.4); padding: 8px 12px; border-radius: 8px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span style="width: 18px; height: 18px; border-radius: 50%; background: ${item.color1.hex}; border: 2px solid white;"></span>
              <span style="font-weight: 700; color: #ffffff;">${item.color1.name}</span>
            </div>
            <button onclick="switchMobileColor('${item.id}', 'c1'); openDetailsModal('${item.id}')" class="tab-pill-btn ${activeColor === 'c1' ? 'active' : ''}" style="padding: 4px 12px; font-size: 0.8rem;">معاينة</button>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(0,0,0,0.4); padding: 8px 12px; border-radius: 8px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span style="width: 18px; height: 18px; border-radius: 50%; background: ${item.color2.hex}; border: 2px solid white;"></span>
              <span style="font-weight: 700; color: #ffffff;">${item.color2.name}</span>
            </div>
            <button onclick="switchMobileColor('${item.id}', 'c2'); openDetailsModal('${item.id}')" class="tab-pill-btn ${activeColor === 'c2' ? 'active' : ''}" style="padding: 4px 12px; font-size: 0.8rem;">معاينة</button>
          </div>
          <button onclick="switchMobileColor('${item.id}', 'dual'); openDetailsModal('${item.id}')" class="tab-pill-btn ${activeColor === 'dual' ? 'active' : ''}" style="width: 100%; text-align: center; margin-top: 4px;">
            عرض اللونين معاً في صورة واحدة
          </button>
        </div>
      </div>
    `;
  }

  body.innerHTML = `
    <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 28px; align-items: center;">
      <div style="background: #060910; border: 1.5px solid var(--gold-border); border-radius: 16px; padding: 20px; display: flex; align-items: center; justify-content: center; min-height: 280px;">
        <img src="${currentImg}" alt="${item.fullName}" style="max-height: 280px; max-width: 100%; object-fit: contain;">
      </div>
      <div>
        <div style="display: flex; gap: 8px; margin-bottom: 8px;">
          <span class="brand-badge ${item.brand.toLowerCase() === 'oppo' ? 'oppo' : 'realme'}">${item.brand}</span>
          ${item.badge ? `<span class="feature-tag">${item.badge}</span>` : ''}
        </div>
        <h2 style="font-size: 1.55rem; font-weight: 900; color: #ffffff; margin-bottom: 12px; line-height: 1.3;">
          ${item.fullName || item.name}
        </h2>

        <div style="background: rgba(212, 175, 55, 0.12); border: 1.5px solid var(--gold-primary); padding: 12px 18px; border-radius: 12px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="font-size: 0.8rem; color: var(--text-muted); display: block;">السعر الرسمي:</span>
            <span style="font-size: 1.85rem; font-weight: 900; color: var(--gold-light);">${formatPrice(item.price)} ج.م</span>
          </div>
          <span style="background: rgba(37, 211, 102, 0.15); color: #4ade80; border: 1px solid rgba(37,211,102,0.3); padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 800;">
            متاح للشحن الفوري
          </span>
        </div>

        ${colorSwitchModalHtml}

        <div style="margin-bottom: 20px;">
          <h4 style="font-size: 0.95rem; color: var(--gold-light); margin-bottom: 8px;">أبرز المواصفات:</h4>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 6px;">
            ${(item.specs || []).map(s => `
              <li style="display: flex; align-items: center; gap: 8px; font-size: 0.88rem; color: #cbd5e1;">
                <i class="fa-solid fa-circle-check" style="color: var(--gold-primary); font-size: 0.85rem;"></i>
                ${s}
              </li>
            `).join('')}
          </ul>
        </div>

        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <button type="button" class="btn-card-buy-instant" style="flex: 1; padding: 13px; font-size: 1rem;" onclick="closeDetailsModal(); buyNow('${item.id}')">
            <i class="fa-solid fa-bolt"></i>
            شراء فوري واستخراج فاتورة
          </button>
          <button type="button" class="btn-card-add-cart" style="padding: 13px 18px;" onclick="addToCart('${item.id}')">
            <i class="fa-solid fa-cart-plus"></i>
            أضف للسلة
          </button>
        </div>
      </div>
    </div>
  `;

  modal.classList.add('active');
}

function closeDetailsModal() {
  const modal = document.getElementById('device-modal');
  if (modal) modal.classList.remove('active');
}

// Toast Notice
function showToast(msg) {
  let toast = document.getElementById('toast-notice');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast-notice';
    toast.className = 'toast-notice';
    document.body.appendChild(toast);
  }
  toast.innerHTML = `<i class="fa-solid fa-circle-check" style="margin-left: 8px;"></i> ${msg}`;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3500);
}
