const nombre = document.querySelector("#nombre");
const monto = document.querySelector("#monto");
const descripcion = document.querySelector("#desc");
const formBoton = document.querySelector(".form-boton");
const listItems = document.querySelector(".items-list");
const total = document.querySelector(".total");

let resultado = 0;

const suma = () => {
  resultado += +monto.value;
  total.textContent = `Total: $ ${resultado}`;
};

const Items = (person) => {
  return `<li id="${person.id}">
						<div class="items-container">
							<div class="nombre-monto">
								<p>${person.nombre}</p>
								<p>$ ${monto.value}</p>
							</div>
							<div class="descripcion">
								<p>${person.descripcion}</p>
							</div>
							<div class="icons-container"> 
								<i id="${person.id}" class="remove">tachito</i>
							</div>
						</div>
					</li>`;
};

const grupoDePersonas = [];

const adherirPersonas = () => {
  if (grupoDePersonas.length === 0) {
    const person = {
      nombre: nombre.value,
      monto: monto.value,
      id: grupoDePersonas.length + 1,
    };

    grupoDePersonas.push(person);
    listItems.innerHTML += Items(person);

    suma();
  }

  // ver si funciona si inicializo la variable como false

  //let existe = false;

  //for (let i = 0; i < grupoDePersonas.length; i++) {
  //if (nombre.value === grupoDePersonas[i].nombre) {
  //existe = true;
  //break;
  //} [> else {
  //existe = nombre.value === grupoDePersonas[i].nombre;
  //} */
  //}

  const existe = grupoDePersonas.find((grup) => nombre.value === grup.nombre);
  //console.log(existe)

  if (existe === undefined) {
    const person = {
      nombre: nombre.value,
      monto: monto.value,
      id: grupoDePersonas.length + 1,
    };

    grupoDePersonas.push(person);

    listItems.innerHTML += Items(person);
    suma();
  }
};

const borrarItems = (itemId) => {
  listItems.removeChild(document.getElementById(itemId));
  const nuevoGrupo = grupoDePersonas.filter(
    (persona) => persona.id !== itemId
  );
  resultado -= nuevoGrupo.reduce((objeto, persona) => {
    return persona.monto
  }, 0)

  //resultado = newGrupOfPeople.reduce((total, persona) => {
    //return total - persona.monto;
  //}, 0);
  //   for (let i = 0; i < listItems.children.length; i++) {
  //     if (listItems.children[i].children[0].children[2].children[0] === item) {
  //       listItems.removeChild(listItems.children[i]);
  //       resultado -= grupoDePersonas[i].monto;
  //       total.textContent = `Total: $ ${resultado}`;
  //       grupoDePersonas.splice(i, 1);
  //     }
  //   }
};

formBoton.addEventListener("click", (e) => {
  e.preventDefault();

  //listItems.innerHTML += Items();
  //suma();
  adherirPersonas();
  //console.log(grupoDePersonas);

  listItems.querySelectorAll(".remove").forEach((rmBtn) => {
    rmBtn.addEventListener("click", () => {
      //console.log(rmBtn.id);
      borrarItems(rmBtn.id);
    });
  });
});
