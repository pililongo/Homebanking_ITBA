let cardCotizaciones = document.querySelector(".cotizaciones");

const regex = /(Dolar)\s[B]/gm;
const regex2 = /(Dolar)\s[OCt]/gm;


fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
.then(data => data.json())
.then(data => data.forEach(element => {
    if (regex.test(element.casa.nombre) || regex2.test(element.casa.nombre)) {
        const usd = {
            nombre: element.casa.nombre,
            compra: element.casa.compra,
            venta: element.casa.venta   
        };

        const Items = (usd) => {
            return `<div class="dolar-div">
                        <p class="dolar-nombre">${usd.nombre}</p>
                        <p class="dolar-compra">Compra $${usd.compra}</p>
                        <p class="dolar-venta">Venta $${usd.venta}</p>
                    </div>`
        }

        cardCotizaciones.innerHTML += Items(usd);
    }
}))
