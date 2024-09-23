function creatToast(label, error) {
  const toastInnerHTML = `
  <div class="toast-header">
    <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#FF4858"></rect></svg>
    <strong class="me-auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    ${label}
    </font></font></strong>
    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fechar"></button>
  </div>
  <div class="toast-body"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    ${error}
  </font></font></div>
  `
  const toastDiv = document.createElement('div');
  toastDiv.classList.add('toast', 'fade', 'show');
  toastDiv.ariaAtomic = true;
  toastDiv.ariaLive = true;
  toastDiv.role = 'alert';
  toastDiv.innerHTML = toastInnerHTML;
  return toastDiv;
}

export { creatToast }
