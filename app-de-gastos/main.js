const nombre = document.querySelector('#nombre');
const monto = document.querySelector('#monto');
const descripcion = document.querySelector('#desc');
const formBoton = document.querySelector('.form-boton');
const listItems = document.querySelector('.items-list');
const total = document.querySelector('.total');

let resultado = 0;

const suma = () => {
	resultado += +monto.value;
	total.textContent = `Total: $ ${resultado}`;
}

const Items = () => {
	return	`<li>
						<div class="items-container">
							<div class="nombre-monto">
								<p>${nombre.value}</p>
								<p>$ ${monto.value}</p>
							</div>
							<div class="descripcion">
								<p>${descripcion.value}</p>
							</div>
							<div class="icons-container"> hola </div>
						</div>
					</li>`
}


formBoton.addEventListener('click', (e) => {
	e.preventDefault();

	listItems.innerHTML += Items();
	suma();
})
