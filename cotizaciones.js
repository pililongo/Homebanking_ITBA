let cardCotizaciones = document.getElementsByClassName("cotizaciones");

let cotizaciones = [];
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
            cotizaciones.push(usd);
        }}));
                
console.log(cotizaciones);