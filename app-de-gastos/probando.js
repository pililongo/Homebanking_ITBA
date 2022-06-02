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
                <p>$ ${person.monto}</p>
              </div>
              <div class="descripcion">
                <p>${person.descripcion}</p>
              </div>
              <div class="icons-container"> 
                <i id="${person.id}" class="remove"><img src="tachito.jpeg" alt=""></i>
              </div>
            </div>
          </li>`
}

const grupoDePersonas = [];

const creaAñade = () => {
    const person = {
      nombre: nombre.value,
      monto: monto.value,
      id: grupoDePersonas.length + 1,
    };

    grupoDePersonas.push(person);
    listItems.innerHTML += Items(person);

    suma();
}

const adherirPersonas = () => {
  if (grupoDePersonas.length === 0) {
    creaAñade();
  }

  const existe = grupoDePersonas.find((grup) => nombre.value === grup.nombre);

  if (existe === undefined) {
    creaAñade();
  }
};

const borrarItems = (itemId) => {
  listItems.removeChild(document.getElementById(itemId));
  const nuevoGrupo = grupoDePersonas.filter(
    (persona) => +itemId === persona.id
  );

  resultado -= nuevoGrupo.reduce((objeto, persona) => {
    return persona.monto;
  }, 0)

  const index = grupoDePersonas.findIndex(grup => { return grup.id === +itemId});
  grupoDePersonas.splice(index, 1);

  total.textContent = `Total: $ ${resultado}`;

};

formBoton.addEventListener("click", (e) => {
  e.preventDefault();

  adherirPersonas();

  listItems.querySelectorAll(".remove").forEach((rmBtn) => {
    rmBtn.addEventListener("click", () => {
      borrarItems(rmBtn.id);
    });
  });
});
