const button = document.querySelector('.hamburger-menu')
const leftBar = document.querySelector('.left-bar')
const content = document.querySelector('.section-grid')


button.addEventListener('click', () => {
	if (leftBar.classList.contains('hidden')) {
		leftBar.classList.remove('hidden');
	} else {
		leftBar.classList.add('hidden');
	}
	if (content.classList.contains('section-grid')){
		content.classList.add('hidden')
		content.classList.remove('section-grid')
	} else {
		content.classList.remove('hidden')
		content.classList.add('section-grid')
	}
})
