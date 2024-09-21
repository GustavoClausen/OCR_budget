const selectSourceLanguage = document.querySelector('#source-language');
const selectTargetLanguage = document.querySelector('#target-language');
const getBudgetForm = document.querySelector('#get-budget-form');
const optTargetLanguage = document.createElement('option');
const inptFiles = document.querySelector('#files');

optTargetLanguage.value = "pd";
optTargetLanguage.innerText = "Selecione o idioma de origem";
optTargetLanguage.disabled = true;
optTargetLanguage.selected = true;

inptFiles.multiple = true;

function clearOptions() {
  for(let option of selectTargetLanguage) {
    if (option.value !== 'pd') {
      option.remove()
      clearOptions();
    }
  }
}

function populateSelect(srcLanguage) {
  if (srcLanguage === 'pt') {
    const optEn = document.createElement('option');
    const optIt = document.createElement('option');
    optEn.value = 'eng';
    optEn.innerText = 'Inglês';
    optIt.value = 'it';
    optIt.innerText = 'Italiano';
    selectTargetLanguage.appendChild(optEn);
    selectTargetLanguage.appendChild(optIt);
  } else {
    const optPt = document.createElement('option');
    optPt.value = 'pt';
    optPt.innerText = 'Português';
    selectTargetLanguage.appendChild(optPt);
  }
}

function showModal() {
  const modal = document.querySelector('.modal');
  modal.classList.add('block');
  setTimeout(() => {
    modal.style.opacity = 1;
  }, 200)
}

function formIsValid() {
  const inptSourceLang = document.querySelector('#source-language').value;
  const inptTargeLang = document.querySelector('#target-language').value;
  if(inptTargeLang === 'pd' || inptSourceLang === 'pd') return false
  if(inptFiles.files.length === 0) return false
  if(inptFiles.files.length === 0) return false
  return true
}

selectSourceLanguage.children[0].innerHTML = 'Selecione o idioma de origem';
selectSourceLanguage.children[0].value = 'pd';
selectSourceLanguage.children[0].selected = true;
selectSourceLanguage.children[0].disabled = true;


selectTargetLanguage.appendChild(optTargetLanguage)

selectSourceLanguage.addEventListener('change', (e) => {
  clearOptions()
  selectTargetLanguage.children[0].innerHTML = 'Selecione o idioma de destino';
  const language = e.target.value;
  populateSelect(language);
});

getBudgetForm.addEventListener('submit', (e) => {
  e.preventDefault();
  if(!formIsValid()) return alert('Preencha todos os campos corretamente.');
  showModal();
  getBudgetForm.submit();
});