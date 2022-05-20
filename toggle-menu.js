const button = document.querySelector('.hamburger-menu')
const leftBar = document.querySelector('.left-bar')


button.addEventListener('click', () => {
	if (leftBar.classList.contains('hidden')) {
		leftBar.classList.remove('hidden');
	} else {
		leftBar.classList.add('hidden');
	}
})
