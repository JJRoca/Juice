// Cuando el documento HTML esté completamente cargado y listo para manipular:
$(document).ready(function() {
    // Maneja el evento clic en los enlaces dentro de elementos con la clase 'categoria-link'
    $('.categoria-link a').on('click', function(e) {
        e.preventDefault(); // Evita que el enlace siga su comportamiento normal

        // Obtiene el atributo 'data-categoria-id' del enlace clickeado
        var categoriaId = $(this).data('categoria-id');
        console.log(categoriaId);

        // Realiza una solicitud AJAX para obtener productos relacionados con la categoría
        $.ajax({
            url: '/consulta-productos/',
            method: 'GET',
            data: { categoriaId: categoriaId },
            dataType: 'json',
            success: function(response) {
                $('#lista-productos').empty(); // Limpia la lista de productos actual
                // Itera a través de los productos recibidos en la respuesta
                $.each(response.productosInternos, function(index, productoInterno) {
                    // Verifica si el producto tiene precios válidos
                    if (productoInterno.precio_p > 0 || productoInterno.precio_m > 0 || productoInterno.precio_g > 0) {
                        let newRow = $('<tr>'); // Crea una nueva fila de tabla

                        newRow.append('<td>' + productoInterno.producto + '</td>'); // Agrega nombre de producto

                        // Agrega celdas de precio según los valores disponibles o celdas vacías
                        if (productoInterno.precio_p > 0) {
                            newRow.append('<td>' + productoInterno.precio_p + ' Bs' + '</td>');
                        } else {
                            newRow.append('<td></td>');
                        }

                        if (productoInterno.precio_m > 0) {
                            newRow.append('<td>' + productoInterno.precio_m + ' Bs' + '</td>');
                        } else {
                            newRow.append('<td></td>');
                        }

                        if (productoInterno.precio_g > 0) {
                            newRow.append('<td>' + productoInterno.precio_g + ' Bs' + '</td>');
                        } else {
                            newRow.append('<td></td>');
                        }

                        newRow.data('select-options', productoInterno.selectOptions); // Establece el atributo data-select-options

                        $('#lista-productos').append(newRow); // Agrega la fila a la lista de productos
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });

    // Maneja el evento clic en filas de la tabla de productos
    $('#lista-productos').on('click', 'tr', function() {
        let producto = $(this).find('td:first').text(); // Obtiene el nombre del producto
        let selectOptions = $(this).data('select-options'); // Obtiene opciones de selección

        let newRow = $('<tr>'); // Crea una nueva fila para detalles
        newRow.append('<td>' + producto + '</td>'); // Agrega el nombre del producto

        newRow.append('<td><select class="fruta-select">' + selectOptions + '</select></td>'); // Agrega select de opciones

        newRow.append('<td><input type="number" class="cantidad-input" min="1" value="1"></td>'); // Agrega input de cantidad

        // Obtiene el valor de la celda en la cual se hizo clic
        let clickedCellValue = $(event.target).closest('td').text();

        // Añade las celdas de precios dinámicamente con el valor de la celda clickeada
        newRow.append('<td class="precio">' + clickedCellValue + '</td>');

        newRow.append('<td class="total">0 Bs</td>'); // Agrega una celda para el total
        newRow.append('<td><input type="text" class="extras-input"></td>'); // Agrega una celda para extras

        $('#lista-detalles').append(newRow); // Agrega la fila a la lista de detalles
    });

    // Maneja el evento clic en el botón "Agregar" en la tabla de detalles
    $('#lista-detalles').on('click', '.agregar-btn', function() {
        let row = $(this).closest('tr');
        var cantidad = row.find('.cantidad-input').val();
        var precio = parseFloat(row.find('.precio').text());
        var total = cantidad * precio;

        row.find('.total').text(total.toFixed(2) + ' Bs'); // Actualiza el total en la fila
        //  actualizarTotalGeneral();
    });

    // Función para calcular y actualizar el total general
    function actualizarTotalGeneral() {
        var totalGeneral = 0;
        // Itera a través de las filas de detalles y suma los totales
        $('#lista-detalles tr').each(function() {
            var totalStr = $(this).find('.total').text();
            var total = parseFloat(totalStr.replace(' Bs', '')) || 0;
            totalGeneral += total;
        });
        // Actualiza el valor en la casilla del total general
        $('#total-general').text(totalGeneral.toFixed(2) + ' Bs');
    }

    // Maneja el cambio en el input de cantidad en la tabla de detalles
    $('#lista-detalles').on('change', '.cantidad-input', function() {
        var row = $(this).closest('tr');
        var cantidad = $(this).val();
        var precio = parseFloat(row.find('.precio').text());

        var total = cantidad * precio;

        row.find('.total').text(total.toFixed(2) + ' Bs');

        // Agrega las propiedades 'precio' y 'total' al objeto 'detalle'
        row.data('precio', precio);
        row.data('total', total);
        actualizarTotalGeneral();
    });

    // Maneja el clic en el botón "Buscar Cliente"
    $('#btnBuscarCliente').on('click', function() {
        $('#buscarClienteContainer').show();
        $('#registrarClienteContainer').hide();
    });

    // Maneja el clic en el botón "Registrar Cliente"
    $('#btnRegistrarCliente').on('click', function() {
        $('#registrarClienteContainer').show();
        $('#buscarClienteContainer').hide();
    });

    // Maneja el clic en el botón "Buscar" para buscar un cliente por NIT
    const buscarClienteNitBtn = document.getElementById('btnBuscar');
    buscarClienteNitBtn.addEventListener('click', function() {
        const nitClienteBuscar = document.getElementById('inputBuscarCliente').value;
        console.log(nitClienteBuscar);

        fetch('/buscar_cliente/?nit=' + nitClienteBuscar)
            .then(response => response.json())
            .then(data => {
                if (data.cliente) {
                    $('#nitCliente').text("NIT: " + data.cliente.nit);
                    $('#nombreCliente').text("Nombre: " + data.cliente.nombre);
                    $('#direccionCliente').text("Dirección: " + data.cliente.direccion);
                    $('#telefonoCliente').text("Teléfono: " + data.cliente.telefono);
                    $('#datosCliente').show();
                    $('#mensajeClienteNoEncontrado').hide();
                } else {
                    $('#datosCliente').hide();
                    $('#mensajeClienteNoEncontrado').show();
                }
            })
            .catch(error => {
                console.log("Error al encontrar datos: " + error);
            });
    });

    // Maneja el clic en el botón "Guardar Venta"
    $('#guardarVenta-btn').on('click', function() {
        var detalles = [];
        var nitCliente = '';

        $('#tabla-detalles tbody tr').each(function() {
            let detalle = {};
            detalle.producto = $(this).find('td:eq(0)').text();
            detalle.ingrediente = $(this).find('td:eq(1) select').val();
            detalle.cantidad = parseInt($(this).find('.cantidad-input').val());
            detalle.precio_venta = parseFloat($(this).find('.precio').text());
            detalle.total_venta = parseFloat($(this).find('.total').text());
            detalle.extras = $(this).find('td:eq(5) input').val();

            detalles.push(detalle);
        });

        // Verificar si se ingresó un NIT de cliente
        if ($('#datosCliente').is(':visible')) {
            nitCliente = $('#nitCliente').text().trim().split(':')[1].trim();
        } else {
            // Se ingresaron los datos de registro de cliente
            var nombreCliente = $('#inputNombre').val().trim();
            nitCliente = $('#inputNit').val().trim();
            var telefonoCliente = $('#inputTelefono').val().trim();

            // Validar los campos requeridos
            if (nombreCliente !== '' && nitCliente !== '' && telefonoCliente !== '') {
                var clienteData = {
                    nombre_cliente: nombreCliente,
                    nit_clienteNuevo: nitCliente,
                    telefono_cliente: telefonoCliente
                };
                detalles.push(clienteData);
            }
            else if (nombreCliente === '' && nitCliente === '' && telefonoCliente === '') {
                // No se ingresaron los datos del cliente, guardar la venta sin el cliente asociado
                detalles.push({});
            } else {
                console.error('Faltan campos requeridos para registrar el cliente');
                return;
            }
        }

        var csrfToken = $('meta[name="csrf-token"]').attr('content');

        // Función para actualizar la tabla de detalles en la plantilla
        function actualizarTablaDetalles(detalles) {
            var tabla = $('#tabla-detalles_pedido');
            tabla.empty();

            detalles.forEach(function(detalle) {
                // Crea filas de tabla y agrega los detalles
                var fila = '<tr>';
                fila += '<td>' + detalle.producto + '</td>';
                fila += '<td>' + detalle.ingrediente + '</td>';
                fila += '<td>' + detalle.cantidad + '</td>';
                // Agrega más columnas según sea necesario
                fila += '</tr>';
                tabla.append(fila);
            });
            console.log("Tabla actualizada con éxito");
        }
        //solicitud a la url guardar_detalles para enviar los datos del front al servidor y se guarde en la db
        $.ajax({
            url: '/guardar_detalles/',
            method: 'POST',
            headers: {
                'X-Csrftoken': csrfToken,
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({
                detalles: detalles,
                nit_cliente: nitCliente
            }),
            success: function(response) {
                console.log("Responseeeeeee", response.message);
                console.log('Detalles guardados exitosamente');
                // Actualiza la tabla de detalles en la plantilla con los nuevos detalles
                console.log("Detalles: ", detalles);
                a = actualizarTablaDetalles(response.detalles);
            },
            error: function(xhr, status, error) {
                console.error('Error al guardar los detalles:', error);
            }
        });

        //solicitud Ajax adicional para cargar la tabla en detalle_factura.html
        $.ajax({
            url: '/detalle_factura/',
            method: 'GET',
            dataType: 'html', // Cambia el tipo de datos a HTML
            success: function(response) {
                // Reemplaza el contenido de detalle_factura.html con la respuesta HTML
                a = document.addEventListener('DOMContentLoaded', function() {
                    var categoriaLinks = document.querySelectorAll('.categoria-link a');

                    categoriaLinks.forEach(function(link) {
                        link.addEventListener('click', function(e) {
                            e.preventDefault();

                            var categoriaId = link.getAttribute('data-categoria-id');
                            console.log(categoriaId);

                            fetch('/consulta-productos/?categoriaId=' + categoriaId)
                                .then(function(response) {
                                    return response.json();
                                })
                                .then(function(data) {
                                    var listaProductos = document.getElementById('lista-productos');
                                    listaProductos.innerHTML = '';

                                    data.productosInternos.forEach(function(productoInterno) {
                                        if (productoInterno.precio_p > 0 || productoInterno.precio_m > 0 || productoInterno.precio_g > 0) {
                                            var newRow = document.createElement('tr');

                                            var productoCell = document.createElement('td');
                                            productoCell.textContent = productoInterno.producto;
                                            newRow.appendChild(productoCell);

                                            if (productoInterno.precio_p > 0) {
                                                var precioPCell = document.createElement('td');
                                                precioPCell.textContent = productoInterno.precio_p + ' Bs';
                                                newRow.appendChild(precioPCell);
                                            } else {
                                                newRow.appendChild(document.createElement('td'));
                                            }

                                            if (productoInterno.precio_m > 0) {
                                                var precioMCell = document.createElement('td');
                                                precioMCell.textContent = productoInterno.precio_m + ' Bs';
                                                newRow.appendChild(precioMCell);
                                            } else {
                                                newRow.appendChild(document.createElement('td'));
                                            }

                                            if (productoInterno.precio_g > 0) {
                                                var precioGCell = document.createElement('td');
                                                precioGCell.textContent = productoInterno.precio_g + ' Bs';
                                                newRow.appendChild(precioGCell);
                                            } else {
                                                newRow.appendChild(document.createElement('td'));
                                            }

                                            newRow.setAttribute('data-select-options', productoInterno.selectOptions);
                                            listaProductos.appendChild(newRow);
                                        }
                                    });
                                })
                                .catch(function(error) {
                                    console.error(error);
                                });
                        });
                    });

                    var listaDetalles = document.getElementById('lista-detalles');
                    listaDetalles.addEventListener('click', function(event) {
                        var target = event.target;
                        if (target.tagName === 'TD') {
                            var producto = target.closest('tr').querySelector('td:first-child').textContent;
                            var selectOptions = target.closest('tr').getAttribute('data-select-options');
                            var newRow = document.createElement('tr');

                            var productoCell = document.createElement('td');
                            productoCell.textContent = producto;
                            newRow.appendChild(productoCell);

                            var selectCell = document.createElement('td');
                            selectCell.innerHTML = '<select class="fruta-select">' + selectOptions + '</select>';
                            newRow.appendChild(selectCell);

                            var cantidadCell = document.createElement('td');
                            cantidadCell.innerHTML = '<input type="number" class="cantidad-input" min="1" value="1">';
                            newRow.appendChild(cantidadCell);

                            var precioCell = document.createElement('td');
                            precioCell.textContent = target.textContent;
                            precioCell.classList.add('precio');
                            newRow.appendChild(precioCell);

                            var totalCell = document.createElement('td');
                            totalCell.textContent = '0 Bs';
                            totalCell.classList.add('total');
                            newRow.appendChild(totalCell);

                            var extrasCell = document.createElement('td');
                            extrasCell.innerHTML = '<input type="text" class="extras-input">';
                            newRow.appendChild(extrasCell);

                            listaDetalles.appendChild(newRow);
                        }
                    });
                    // Función para calcular y actualizar el total general
                    function actualizarTotalGeneral() {
                        var totalGeneral = 0;
                        var detalleRows = document.querySelectorAll('#lista-detalles tr');

                        detalleRows.forEach(function(row) {
                            var totalStr = row.querySelector('.total').textContent;
                            var total = parseFloat(totalStr.replace(' Bs', '')) || 0;
                            totalGeneral += total;
                        });

                        var totalGeneralCell = document.getElementById('total-general');
                        totalGeneralCell.textContent = totalGeneral.toFixed(2) + ' Bs';
                    }
                });
                $('#tabla-detalles_pedido').html(response);
                console.log('Solicitud AJAX exitosa', $('#tabla-detalles_pedido').html());
            },
            error: function(xhr, status, error) {
                console.error('Error al cargar la tabla de detalle_factura:', error);
                console.log('Solicitud AJAX erronea'); // Agrega un mensaje de éxito
            }
        });
    });

    // Obtén la referencia a las tablas
    const tablaProductos = document.getElementById("tabla-productos");
    const tablaDetalles = document.getElementById("tabla-detalles");

    // Calcula y ajusta la altura de la tabla-detalles
    function ajustarAlturaTablaDetalles() {
        const numFilas = tablaProductos.rows.length;
        const alturaTabla = numFilas * 40; // Ajusta el valor según tus necesidades

        tablaDetalles.style.height = `${alturaTabla}px`;
    }

    // Llama a la función para ajustar la altura inicialmente y cuando haya cambios en la tabla-productos
    ajustarAlturaTablaDetalles();
});
