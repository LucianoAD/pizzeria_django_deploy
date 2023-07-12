// Obtener los datos de las pizzas desde la URL
fetch('pizzas/pizzas-json/')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Recorrer los datos y crear las tarjetas en el DOM
        data.pizza.forEach(pizza => {
            const tarjeta = document.createElement('div');
            tarjeta.classList.add('tarjeta');

            const imagen = document.createElement('img');
            imagen.src = pizza.ruta;
            imagen.alt = pizza.nombre;

            const nombre = document.createElement('h3');
            nombre.textContent = pizza.nombre;

            const descripcion = document.createElement('p');
            descripcion.textContent = pizza.descripcion;

            tarjeta.appendChild(imagen);
            tarjeta.appendChild(nombre);
            tarjeta.appendChild(descripcion);

            // Agregar la tarjeta al contenedor en el DOM
            const tarjetasContainer = document.getElementById('tarjetas-container');
            tarjetasContainer.appendChild(tarjeta);
        });
    })
    .catch(error => console.log('Error al obtener los datos de las pizzas:', error));
