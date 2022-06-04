const nombre = document.querySelector("#nombre");
const monto = document.querySelector("#monto");
const descripcion = document.querySelector("#desc");
const formBoton = document.querySelector(".form-boton");
const listItems = document.querySelector(".items-list");
const total = document.querySelector(".total");

let resultado = 0;

function ConfirmDelete(){
  var respuesta = confirm ("¿Estás seguro que deseas eliminar este gasto?");
  if (respuesta == true)
  {
    return true;
  }
  else
  {
    return false;
  }
}

const Items = (person) => {
	return `<li id="${person.id}">
            <div class="items-container">
              <div class="nombre-monto">
                <p>${person.nombre}</p>
    <p  id="total-${person.nombre}" class="total-persona"> Total: $ ${person.monto.toLocaleString()}</p>
              </div>
              <div id="${person.nombre}" class="descripcion">
                <p>${person.descripcion} $${person.monto.toLocaleString()}</p>
              </div>
              <div class="icons-container"> 
									<i id="${person.id}" class="fa-solid fa-trash-can remove"></i>
              </div>
            </div>
          </li>`
}

const Descripcion = (descripcion, monto) => {
  return `<p>${descripcion} $${monto}</p>`
}

const grupoDePersonas = [];

const creaAñade = () => {
    const person = {
      nombre: nombre.value,
      monto: +monto.value,
      descripcion: descripcion.value,
      id: grupoDePersonas.length + 1,
    };

    grupoDePersonas.push(person);
    listItems.innerHTML += Items(person);
}

const adherirPersonas = () => {
  const existe = grupoDePersonas.find((grup) => nombre.value === grup.nombre);

  if (existe && grupoDePersonas.length > 0) {

    const divDescripcion = document.querySelector(`#${existe.nombre}`);
    const totalPersona = document.querySelector(`#total-${existe.nombre}`);

    divDescripcion.innerHTML += Descripcion(descripcion.value, Number(monto.value).toLocaleString());
    
    grupoDePersonas.forEach((grup) => {
      if (existe.nombre === grup.nombre) {
        grup.monto += +monto.value;
        totalPersona.textContent = `Total: $ ${grup.monto.toLocaleString()}`;
      }
    })
    
  }

  if (existe === undefined) {
    creaAñade();
  }

  let totalTotal = 0;

  grupoDePersonas.forEach((grup) => {
    totalTotal += grup.monto;
  })
  resultado = totalTotal;
  total.textContent = `Total: $ ${totalTotal.toLocaleString()}`;
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

  total.textContent = `Total: $ ${resultado.toLocaleString()}`;

};

formBoton.addEventListener("click", (e) => {
  e.preventDefault();

  adherirPersonas();

  listItems.querySelectorAll(".remove").forEach((rmBtn) => {
    rmBtn.addEventListener("click", () => {
      // ConfirmDelete();
      if (ConfirmDelete() === true){ 
        borrarItems(rmBtn.id);
      }
    });
  });
});
