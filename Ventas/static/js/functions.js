$(document).ready(function(){
    //--------------------- SELECCIONAR FOTO PRODUCTO ---------------------
    $("#foto").on("change",function(){
    	var uploadFoto = document.getElementById("foto").value;
        var foto       = document.getElementById("foto").files;
        var nav = window.URL || window.webkitURL;
        var contactAlert = document.getElementById('form_alert');
        
            if(uploadFoto !='')
            {
                var type = foto[0].type;
                var name = foto[0].name;
                if(type != 'image/jpeg' && type != 'image/jpg' && type != 'image/png')
                {
                    contactAlert.innerHTML = '<p class="errorArchivo">El archivo no es válido.</p>';                        
                    $("#img").remove();
                    $(".delPhoto").addClass('notBlock');
                    $('#foto').val('');
                    return false;
                }else{  
                        contactAlert.innerHTML='';
                        $("#img").remove();
                        $(".delPhoto").removeClass('notBlock');
                        var objeto_url = nav.createObjectURL(this.files[0]);
                        $(".prevPhoto").append("<img id='img' src="+objeto_url+">");
                        $(".upimg label").remove();
                        
                    }
              }else{
              	alert("No selecciono foto");
                $("#img").remove();
              }              
    });
    $('.delPhoto').click(function(){
    	$('#foto').val('');
    	$(".delPhoto").addClass('notBlock');
    	$("#img").remove();
        
        if ($("#foto_actual") && $("#foto_remove")) {
            $("#foto_remove").val('img_producto.png');
        }

    });
    //modal form delete
    $('.del_product').click(function(e) {
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var producto = $(this).attr('product');
        var action = 'infoProducto';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion de envio
            type: "POST",//tipo de envio
            async:true,//retorno de valor
            data: {action:action, producto:producto}, //datos enviados
            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);// codigo html para mostrar en la vista
                    $('.bodyModal').html('<form action="" method="post" name="form_del_product" id="form_del_product" onsubmit="event.preventDefault(); delProduct();">'+
                    '<h1><i class="fa-solid fa-boxes-packing fa-3x"></i><br><br> Eliminar Producto</h1>'+
                    '<h2>¿Esta seguro de eliminar el siguiente producto?</h2><br>'+
                    '<h2 class="nameProducto">'+info.descripcion+' </h2>'+
                    '<h2 class="cantidadProducto">'+info.existencia+'</h2>'+
                    '<h2 class="precioProducto">'+info.precio+'</h2>'+
                    '<input type="hidden" name="producto_id" id="producto_id" value='+info.codproducto_ex+' required>'+
                    '<input type="hidden" name="action" value="delProduct" required>'+
                    '<div class="alert alertAddProduct"></div>' +
                    '<button type="submit" value="Eliminar" class="btn_ok"><i class="fa-solid fa-trash"></i> Eliminar</button>'+
                    '<a class="btn_cancel" onclick="closeModal();"><i class="fa-solid fa-ban"></i> Cerrar</a>'+
                '</form>');
                }
            },
            error: function(error){
                console.log(error);
            }
        });

        $('.modal').fadeIn();
    });
    //eliminar usuario
    $('.delelteUser').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var idUsuario = $(this).attr('usuarioDelete');
        var action = 'infoUsuario';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion de envio
            type: "POST", //tipo de envio
            async:true, // retorno de valor
            data: {action:action, idUsuario:idUsuario}, //datos que se enviaran
            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo hmtl para mostrar en la vista
                    $('.bodyModal').html('<form action="" method="post" name="form_del_usuario" id="form_del_usuario" onsubmit="event.preventDefault(); delUser();">'+
                    '<h1><i class="fa-solid fa-user-xmark fa-4x" style="color:#e66262;"></i><br><br> Eliminar Usuario</h1>'+
                    '<h2>¿Esta seguro de eliminar el siguiente usuario?</h2><br>'+
                    '<h2 class="nameProducto">'+info.nombre+' </h2>'+
                    '<h2 class="cantidadProducto">'+info.correo+'</h2>'+
                    '<h2 class="precioProducto">'+info.usuario+'</h2>'+
                    '<input type="hidden" name="usuario_id" id="usuario_id" value='+info.idusuario+' required>'+
                    '<input type="hidden" name="action" value="delUsuario" required>'+
                    '<div class="alert alertAddProduct"></div>' +
                    '<button type="submit" value="Eliminar" class="btn_ok"><i class="fa-solid fa-trash"></i> Eliminar</button>'+
                    '<a class="btn_cancel" onclick="closeModal();"><i class="fa-solid fa-ban"></i> Cerrar</a>'+
                    '</form>');
                }
            },
            error: function(error){
                console.log(error);
            }
        });

        $('.modal').fadeIn();
        
    });
    //eliminar cliente
    $('.deleteCliente').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var idcliente = $(this).attr('clienteDelete');
        var action = 'infoCliente';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion de envio
            type: "POST",//tipo de envio
            async:true, //retorno de resultado
            data: {action:action, idcliente:idcliente},//datos que se enviaran

            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo html para mostrar en la interfaz
                    $('.bodyModal').html('<form action="" method="post" name="form_del_cliente" id="form_del_cliente" onsubmit="event.preventDefault(); delCliente();">'+
                    '<h1><i class="fa-solid fa-user-xmark fa-4x" style="color:#e66262;"></i><br><br> Eliminar Cliente</h1>'+
                    '<h2>¿Esta seguro de eliminar el siguiente cliente?</h2><br>'+
                    '<h2>'+info.ci+' </h2>'+
                    '<h2>'+info.nombre+'</h2>'+
                    '<h2>'+info.telefono+'</h2>'+
                    '<h2>'+info.direccion+'</h2>'+
                    '<input type="hidden" name="cliente_id" id="cliente_id" value='+info.idcliente+' required>'+
                    '<input type="hidden" name="action" value="delCliente" required>'+
                    '<div class="alert alertAddProduct"></div>' +
                    '<button type="submit" value="Eliminar" class="btn_ok"><i class="fa-solid fa-trash"></i> Eliminar</button>'+
                    '<a class="btn_cancel" onclick="closeModal();"><i class="fa-solid fa-ban"></i> Cerrar</a>'+
                    '</form>');
                }
            },
            error: function(error){
                console.log(error);
            }
        });

        $('.modal').fadeIn();
    });
    //elimianr proveedor
    $('.deleteProveedor').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var idproveedor = $(this).attr('proveedorDelete');
        var action = 'infoProveedor';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion de envio
            type: "POST",//tipo de envio
            async:true,//retorno de datos
            data: {action:action, idproveedor:idproveedor},//datos enviados

            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo html que se mostrara en la interfaz
                    $('.bodyModal').html('<form action="" method="post" name="form_del_proveedor" id="form_del_proveedor" onsubmit="event.preventDefault(); delProveedor();">'+
                    '<h1><i class="fa-solid fa-building-circle-xmark fa-4x" style="color:#e66262;"></i><br><br> Eliminar Proveedor</h1>'+
                    '<h2>¿Esta seguro de eliminar el siguiente proveedor?</h2><br>'+
                    '<h2>'+info.proveedor+' </h2>'+
                    '<h2>'+info.contacto+'</h2>'+
                    '<h2>'+info.telefono+'</h2>'+
                    '<h2>'+info.direccion+'</h2>'+
                    '<input type="hidden" name="proveedor_id" id="proveedor_id" value='+info.codproveedor+' required>'+
                    '<input type="hidden" name="action" value="delProveedor" required>'+
                    '<div class="alert alertAddProduct"></div>' +
                    '<button type="submit" value="Eliminar" class="btn_ok"><i class="fa-solid fa-trash"></i> Eliminar</button>'+
                    '<a class="btn_cancel" onclick="closeModal();"><i class="fa-solid fa-ban"></i> Cerrar</a>'+
                    '</form>');
                }
            },
            error: function(error){
                console.log(error);
            }
        });

        $('.modal').fadeIn();
    });
    //modal form delete interno
    $('.del_product_in').click(function(e) {
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var producto_in = $(this).attr('producto_In');
        var action = 'infoProductoIn';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            async:true,//retorno de datos
            data: {action:action, producto_in:producto_in},//datos de envio
            success: function(response){
                if (response != 'error') {
                    //console.log(response);
                    var info = JSON.parse(response);//codigo html para mostra en la interfaz
                    $('.bodyModal').html('<form action="" method="post" name="form_del_product_in" id="form_del_product_in" onsubmit="event.preventDefault(); delProductIn();">'+
                    '<h1><i class="fa-solid fa-boxes-packing fa-3x"></i><br><br> Eliminar Producto</h1>'+
                    '<h2>¿Esta seguro de eliminar el siguiente producto?</h2><br>'+
                    '<h2 class="nameProducto">'+info.descripcion+' </h2>'+
                    '<h2 class="nameProducto">'+info.categoria+' </h2>'+
                    '<h2 class="nameProducto">'+info.existencia+' </h2>'+
                    '<h2 class="cantidadProducto">'+info.proveedor+'</h2>'+
                    '<h2 class="precioProducto">'+info.date_add+'</h2>'+
                    '<input type="hidden" name="producto_id" id="producto_id" value='+info.codproducto_in+' required>'+
                    '<input type="hidden" name="action" value="delProductIn" required>'+
                    '<div class="alert alertAddProduct"></div>' +
                    '<button type="submit" value="Eliminar" class="btn_ok"><i class="fa-solid fa-trash"></i> Eliminar</button>'+
                    '<a class="btn_cancel" onclick="closeModal();"><i class="fa-solid fa-ban"></i> Cerrar</a>'+
                '</form>');
                }
            },
            error: function(error){
                console.log(error);
            }
        });

        $('.modal').fadeIn();
    });
    //agregar producto Pequeño
    $('.add_product_in_p').click(function(e) {
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var producto = $(this).attr('producto_In_P');
        var categoria = $(this).attr('cat_In_P');
        var action = 'addProductoDetalle_p';
        var cantidad = 1;
        var tamano = 'P';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            async:true,//retorno de datos
            data: {action:action, producto:producto, categoria:categoria, cantidad:cantidad, tamano:tamano},//datos enviados
            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo html para la vista
                    $('#detalle_venta').html(info.detalle);
                    $('#detalle_totales').html(info.totales);
                    viewProcesar();
                }else{
                    console.log('no data');
                } 
            },
            error: function(error){
                console.log(error);
            }
        });
    });
    //mostrar ingredientes del producto
    $('.list_view').click(function(e) {
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var idproducto_p = $(this).attr('producto_In_P');
        var action = 'list_ingredients_list';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST", //tipo de envio
            async:true, //retorno de resultados
            data: {action:action, idproducto_p:idproducto_p}, //datos enviados
            cache:"false",
            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo html para la vista
                    $('#list_ingredients').html(info.listaIngredientes);
                    viewProcesar();
                }else{
                    console.log('no data');
                } 
            },
            error: function(error){
                console.log(error);
            }
        });
            
    });
    //agregar venta mediano
    $('.add_product_in_m').click(function(e) {
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var producto = $(this).attr('producto_In_M');
        var categoria = $(this).attr('cat_In_M');
        var action = 'addProductoDetalle_m';
        var cantidad = 1;
        var tamano = 'M';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            async:true,  //retorno de resultado
            data: {action:action, producto:producto, categoria:categoria, cantidad:cantidad, tamano:tamano},//datos enviados
            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo html para la vista
                    $('#detalle_venta').html(info.detalle);
                        $('#detalle_totales').html(info.totales);
                        viewProcesar();
                }else{
                    console.log('no data');
                } 
            },
            error: function(error){
                console.log(error);
            }
        });
    });             
    //agregar venta grande
    $('.add_product_in_g').click(function(e) {
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var producto = $(this).attr('producto_In_G');
        var categoria = $(this).attr('cat_In_G');
        var action = 'addProductoDetalle_g';
        var cantidad = 1;
        var tamano = 'G';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            async:true,  //retorno de datos
            data: {action:action, producto:producto, categoria:categoria, cantidad:cantidad, tamano:tamano},//datos enviados
            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo hmtl para la vista
                    $('#detalle_venta').html(info.detalle);
                    $('#detalle_totales').html(info.totales);
                    viewProcesar();
                }else{
                    console.log('no data');
                } 
            },
            error: function(error){
                console.log(error);
            }
        });
    });
    //busqueda en la parte del proveedor
    $('#search_proveedor').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        /**
         * obtenemos los valores los input para el redireccionamiento de busqueda
         */
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_tipo').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&tipo='+$('#search_tipo').val() + '&concepto='+$('#search_concepto').val();
        }else 
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_tipo').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&tipo='+$('#search_tipo').val();
        }else
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&concepto='+$('#search_concepto').val();
        }else
        if($('#search_tipo').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val() + '&tipo='+$('#search_tipo').val() + '&concepto='+$('#search_concepto').val() ;
        }else
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val();
        }else
        if ($('#search_tipo').val() != '') {
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val() + '&tipo='+$('#search_tipo').val();
        }else 
        if($('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val() + '&concepto='+$('#search_concepto').val();
        }else{
            location.href = sistema + 'buscar_producto_ex.php?proveedor='+$(this).val();
        }
    });
    //busqueda en la parte del tipo
    $('#search_tipo').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        /**
         * obtenemos los valores los input para el redireccionamiento de busqueda
         */
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_proveedor').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&proveedor='+$('#search_proveedor').val() + '&concepto='+$('#search_concepto').val();
        }else 
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_proveedor').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&proveedor='+$('#search_proveedor').val();
        }else
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&concepto='+$('#search_concepto').val();
        }else
        if($('#search_concepto').val() != '' && $('#search_proveedor').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val() + '&concepto='+$('#search_concepto').val() + '&proveedor='+$('#search_proveedor').val();
        }else
        if ($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '') {
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val();
        }else
        if ($('#search_proveedor').val() != '') {
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val() + '&proveedor='+$('#search_proveedor').val();
        }else 
        if($('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val() + '&concepto='+$('#search_concepto').val();
        }else{
            location.href = sistema + 'buscar_producto_ex.php?tipo='+$(this).val();
        }
    });
    //busqueda en la parte del concepto
    $('#search_concepto').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        /**
         * obtenemos los valores los input para el redireccionamiento de busqueda
         */
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_proveedor').val() != '' && $('#search_tipo').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&proveedor='+$('#search_proveedor').val() + '&tipo='+$('#search_tipo').val();
        }else 
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_proveedor').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&proveedor='+$('#search_proveedor').val();
        }else
        if($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != '' && $('#search_tipo').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&tipo='+$('#search_tipo').val();
        }else
        if($('#search_tipo').val() != '' && $('#search_proveedor').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val() + '&tipo='+$('#search_tipo').val() + '&proveedor='+$('#search_proveedor').val();
        }else
        if ($('#ex_fecha_de').val() != '' && $('#ex_fecha_a').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val() + '&ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val();
        }else
        if ($('#proveedor').val() != '') {
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val() + '&proveedor='+$('#search_proveedor').val();
        }else 
        if($('#search_tipo').val() != '') {
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val() + '&tipo='+$('#search_tipo').val();
        }else{
            location.href = sistema + 'buscar_producto_ex.php?concepto='+$(this).val();
        }
    });
    /*producto_externo buscador fecha*/
    $('#ex_fecha_de')+$('#ex_fecha_a').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        /**
         * obtenemos los valores los input para el redireccionamiento de busqueda
         */
        if($('#search_proveedor').val() != '' && $('#search_tipo').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&concepto='+$('#search_concepto').val() + '&proveedor='+$('#search_proveedor').val() + '&tipo='+$('#search_tipo').val();
        }else
        if($('#search_proveedor').val() != '' && $('#search_tipo').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&proveedor='+$('#search_proveedor').val() + '&tipo='+$('#search_tipo').val();
        }else
        if($('#search_proveedor').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&proveedor='+$('#search_proveedor').val() + '&tipo='+$('#search_tipo').val();
        }else
        if($('#search_tipo').val() != '' && $('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&concepto='+$('#search_concepto').val() + '&tipo='+$('#search_tipo').val();
        }else
        if($('#search_tipo').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&tipo='+$('#search_tipo').val();
        }else
        if($('#search_concepto').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&concepto='+$('#search_concepto').val();
        }else
        if($('#search_proveedor').val() != ''){
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val() + '&proveedor='+$('#search_proveedor').val();
        }else{
            location.href = sistema + 'buscar_producto_ex.php?ex_fecha_de='+$('#ex_fecha_de').val() + '&ex_fecha_a='+$('#ex_fecha_a').val();
        }

    });
    /*fin producto_externo buscador fecha*/
    $('#busqueda').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        location.href = sistema + 'buscar_usuario.php?busqueda='+$(this).val();
    });
    //busqueda en la parte del cliente
    $('#busqueda_c').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        location.href = sistema + 'buscar_cliente.php?busqueda_c='+$(this).val();
    });
    //busqueda en la parte del proveedor
    $('#busqueda_p').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        location.href = sistema + 'buscar_proveedor.php?busqueda_p='+$(this).val();
    });
    //busqueda en la parte del producto interno
    $('#busqueda_in').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        location.href = sistema + 'buscar_producto_in.php?busqueda_in='+$(this).val();
    });
    /*producto_interno buscador fecha*/
    $('#search_categoria').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        if ($('#fecha_de').val() != '' && $('#fecha_a').val() != '' && $('#search_precio').val() != '') {
            location.href = sistema + 'buscar_producto_in.php?categoria='+$(this).val() + '&fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val() + '&precio='+$('#search_precio').val();
        }else
        if ($('#fecha_de').val() != '' && $('#fecha_a').val() != '') {
            location.href = sistema + 'buscar_producto_in.php?categoria='+$(this).val() + '&fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val();
        }else
        if ($('#search_precio').val() != ''){
            location.href = sistema + 'buscar_producto_in.php?categoria='+$(this).val() + '&precio='+$('#search_precio').val();
        }else{
            location.href = sistema + 'buscar_producto_in.php?categoria='+$(this).val();
        }
    });
    //busqueda por el precio
    $('#search_precio').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        if ($('#fecha_de').val() != '' && $('#fecha_a').val() != '' && $('#search_categoria').val() != '') {
            location.href = sistema + 'buscar_producto_in.php?precio='+$(this).val() + '&fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val() + '&categoria='+$('#search_categoria').val();
        }else
        if ($('#fecha_de').val() != '' && $('#fecha_a').val() != '') {
            location.href = sistema + 'buscar_producto_in.php?precio='+$(this).val() + '&fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val();
        }else
        if ($('#search_categoria').val() != ''){
            location.href = sistema + 'buscar_producto_in.php?precio='+$(this).val() + '&categoria='+$('#search_categoria').val();
        }else{
            location.href = sistema + 'buscar_producto_in.php?precio='+$(this).val();
        }
    });
    //busqueda por fecha
    $('#fecha_de')+$('#fecha_a').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        if ($('#search_precio').val() != '' && $('#search_categoria').val() != '') {
            location.href = sistema + 'buscar_producto_in.php?fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val() + '&categoria='+ $('#search_categoria').val() + '&precio='+$('#search_precio').val();
        }else
        if ($('#search_categoria').val() != '') {
            location.href = sistema + 'buscar_producto_in.php?fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val() + '&categoria='+ $('#search_categoria').val();
        }else
        if ($('#search_precio').val() != ''){
            location.href = sistema + 'buscar_producto_in.php?fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val() + '&precio='+$('#search_precio').val();
        }else{
            location.href = sistema + 'buscar_producto_in.php?fecha_de='+$('#fecha_de').val() + '&fecha_a='+$('#fecha_a').val();
        }
    });
    /*fin producto_interno buscador fecha*/
    /*lista-venta buscador fecha*/
    $('#busqueda_v').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        location.href = sistema + 'buscar_venta.php?busqueda_v='+$('#busqueda_v').val();
    });
    //buscador de venta por fecha
    $('#v_fecha_de')+$('#v_fecha_a').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        location.href = sistema + 'buscar_venta.php?v_fecha_de='+$('#v_fecha_de').val() + '&v_fecha_a='+$('#v_fecha_a').val();
    });
    /*final lista-venta buscador fecha*/
    //busqueda por categoria venta
    $('#search_categoria_venta').change(function(e){
        e.preventDefault();
        var sistema = getUrl();
        location.href = sistema + 'categoria_venta.php?categoria='+$(this).val();
    });
    //habilitar espacios para el registro de un nuevo cliente
    $('.btn_new_cliente').click(function(e){
        e.preventDefault();
        $('#nom_cliente').removeAttr('disabled');
        $('#tel_cliente').removeAttr('disabled');
        $('#dir_cliente').removeAttr('disabled');

        $('#div_registro_cliente').slideDown();
    });
    //Buscar Cliente
    $('#ci_cliente').keyup(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var cl = $(this).val();
        var action = 'searchCliente';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            async: true,//retorno de resultado
            data: {action:action, cliente:cl},//datos enviados
            success: function (response) {
                if (response == 0) {//si la respuesta es 0, los inputs estaran vacios
                    $('#idcliente').val('');
                    $('#nom_cliente').val('');
                    $('#tel_cliente').val('');
                    $('#dir_cliente').val('');

                    //mostra el boton agregar

                    $('.btn_new_cliente').slideDown();
                }else{//si no, los inputs estaran se llenaran con los resultados
                    var data = $.parseJSON(response);
                    $('#idcliente').val(data.idcliente);
                    $('#nom_cliente').val(data.nombre);
                    $('#tel_cliente').val(data.telefono);
                    $('#dir_cliente').val(data.direccion);

                    //ocultar el boton agregar

                    $('.btn_new_cliente').slideUp();
                    //Bloque campos
                    $('#nom_cliente').attr('disabled','disabled');
                    $('#tel_cliente').attr('disabled','disabled');
                    $('#dir_cliente').attr('disabled','disabled');

                    //oculta el boton guardar
                    $('#div_registro_cliente').slideUp();
                }
            },
            error: function(error){

            }
        });
    });
    //Crear cliente ventas
    $('#form_new_cliente_venta').submit(function(e){
        e.preventDefault();
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//ruta o direccion de envio
            type: "POST",//tipo de envio
            async : true,//retorno de resultados
            data: $('#form_new_cliente_venta').serialize(),
            success: function (response) {
                //Agregar id a input hiden
                $('#idcliente').val(response);
                //Bloque campos
                $('#nom_cliente').attr('disabled','disabled');
                $('#tel_cliente').attr('disabled','disabled');
                $('#dir_cliente').attr('disabled','disabled');

                //ocualta el boton para agregar

                $('.btn_new_cliente').slideUp();
                $('#div_registro_cliente').slideUp();
            },
            error: function(error){

            }
        });
    });
    //btn_anular todo
    $('#btn_anular_venta').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var rows = $('#detalle_venta tr').length;
        if (rows > 0) {
            var action = 'anularVenta';
            /**
             * ajax nos permite enviar datos a un lugar determinado
             */ 
            $.ajax({
                url: "../../ajax.php",//direccion o ruta de envio
                type: "POST",//tipo de envio
                data: {action:action},//datos enviados
                async: true,//retorno de resultado
                success: function (response) {
                    if (response != 'error') {
                        location.reload();//recargar la pagina
                    }
                },
                error: function(error){
                    
                }
            });
        }
    });
    //proceder venta
    $('#btn_facturar_venta').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var rows = $('#detalle_venta tr').length;
        if (rows > 0) {
            var action = 'procesarVenta';
            var codcliente = $('#idcliente').val();
            /**
             * ajax nos permite enviar datos a un lugar determinado
             */ 
            $.ajax({
                url: "../../ajax.php",//direccion o ruta de envio
                type: "POST",//tipo de envio
                data: {action:action, codcliente:codcliente},//daros enviados
                async: true,//restorno de resultados
                success: function (response) {
                    if (response != 'error') {
                        var info = JSON.parse(response);
                        facturaTxt(info.codcliente, info.nofactura);//funcion factura
                        $(location).attr('href','nueva_venta.php');//redireccionamiento
                    }else{
                        console.log('no data');
                    }
                },
                error: function(error){
                    
                }
            });
        }
    });
    //Anular venta y/ o factura
    $('.anular_factura').click(function(e) {
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var nofactura = $(this).attr('fac');
        var action = 'infoFactura';
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */ 
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            data: {action:action, nofactura:nofactura},//datos enviados
            async:true,//retorno de resultadp
            success: function(response){
                if (response != 'error') {
                    var info = JSON.parse(response);//codigo html para la vista
                    $('.bodyModal').html('<form action="" method="post" name="form_anular_factura" id="form_anular_factura" onsubmit="event.preventDefault(); anularFactura();">'+
                    '<h1><i class="fa-solid fa-ban fa-3x"></i><br><br> Anular Factura</h1>'+
                    '<h2>¿Esta seguro de anular la factura?</h2><br>'+
                    '<p><strong>No. '+info.nofactura+'</strong></p>'+
                    '<p><strong>Monto Bs. '+info.totalfactura+'</strong></p>'+
                    '<p><strong>Fecha. '+info.fecha+'</strong></p>'+
                    '<input type="hidden" name="action" value="anularFactura">'+
                    '<input type="hidden" name="no_factura" id="no_factura" value="'+info.nofactura+'" required></input>'+
                    '<div class="alert alertAddProduct"></div>' +
                    '<button type="submit" value="Eliminar" class="btn_ok"><i class="fa-solid fa-trash"></i> Anular</button>'+
                    '<a class="btn_cancel" onclick="closeModal();"><i class="fa-solid fa-ban"></i> Cerrar</a>'+
                '</form>');
                
                }
            },
            error: function(error){
                console.log(error);
            }
        });

        $('.modal').fadeIn();
    });
    //ver Factura
    $('.view_factura').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var codcliente = $(this).attr('cl');
        var noFactura = $(this).attr('f');
        window.location.replace("../../resources/venta/vistaVenta.php?idcliente="+codcliente+"&nofactura="+noFactura);//redireccionamiento de pagina
    });
    //toast notificacion
    if ($('#pedido_detalle').html()) {
        notify();
    }
    //efecto de ondas de agua
    $('.fondo-efecto-ondas').ripples({
        resolution: 512,
        dropRadius: 20,
        perturbance: 0.01,
    });
    //activar o desctivar los inputs cuando se seleccione la opcion usuario
    $('#op_usuario').click(function(){
        $('#nombre').removeAttr('disabled');
        $('#correo').removeAttr('disabled');
        $('#usuario').removeAttr('disabled');
        $('#clave').removeAttr('disabled');
        $('#rol').removeAttr('disabled');
        $('#op_socio').prop('checked', false);
    });
    //activar o desactivar los inputs cuando se seleccione la opcion socio
    $('#op_socio').click(function(){
        $('#nombre').removeAttr('disabled');
        $('#correo').prop('disabled', true);
        $('#usuario').removeAttr('disabled');
        $('#clave').prop('disabled', true);
        $('#rol').prop('disabled', true);
        $('#op_usuario').prop('checked', false);
    });
    //check para levar todo el pedido
    $('.everythingToGo' ).on( 'click', function() {
        if( $(this).is(':checked') ){
        /**
         * variables en donde se guardaran los valor obtenidos
         */
            var action = 'paraLlevar';
            var llevar = $(this).val();
            $.ajax({
                url: "../../ajax.php",//direccion o ruta de envio
                type: "POST",//tipo de envio
                data: {action:action, llevar:llevar},//datos enviados
                async:true,//retorno de datos
                success: function(response){
                    if (response != 'error') {
                        location.reload();//refrescar la pagina
                    }
                },
                error: function(error){
                    console.log(error);
                }
            });
        } /*else {
            // Hacer algo si el checkbox ha sido deseleccionado
            //alert("El checkbox con valor " + $(this).val() + " ha sido deseleccionado");
        }*/
    });
    /*$('.date_cantidad').change(function(e){
        e.preventDefault();
        alert($(this).val());
    });*/
    //editar la venta unitaria
    $('.venta_unitario').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var action = 'VentaUnitario';
        var correlativo = $(this).attr('correlativo');
        var total = $('.total_venta').val();
        var nofactura = $(this).attr('nofactura');
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de encio
            data: {action:action, correlativo:correlativo, total:total, nofactura:nofactura},//datos enviados
            async:true,//retorno de resultados
            success: function(response){
                if (response != 'error') {
                    location.reload();//refrescar la pagina
                }
            },
            error: function(error){
                console.log(error);
            }
        });
    });
    //restaurar la venta unitaria
    $('.restaurar_venta_unitario').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var action = 'RestaurarVentaUnitario';
        var correlativo = $(this).attr('correlativo');
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            data: {action:action, correlativo:correlativo},//datos enviados
            async:true,//retorno de resultado
            success: function(response){
                if (response != 'error') {
                    location.reload();//refrescar la pagina
                }
            },
            error: function(error){
                console.log(error);
            }
        });
    });
    //actualizar la venta unitaria
    $('.atualizar_factura').click(function(e){
        e.preventDefault();
        /**
         * variables en donde se guardaran los valor obtenidos
         */
        var action = 'ActualizarFactura';
        var total = $('.total_venta').val();
        var nofactura = $(this).attr('nofactura');
        /**
         * ajax nos permite enviar datos a un lugar determinado
         */
        $.ajax({
            url: "../../ajax.php",//direccion o ruta de envio
            type: "POST",//tipo de envio
            data: {action:action, total:total, nofactura:nofactura},//datos enviados
            async:true,//retorno de resultado
            success: function(response){
                if (response != 'error') {
                    location.reload();//refrescar pagina
                }
            },
            error: function(error){
                console.log(error);
            }
        });
    })  
    
});

//anular Factura
function anularFactura () {
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var noFactura = $('#no_factura').val();
    var action = 'anularFactura';
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        type: "POST",//
        url: "../../ajax.php",
        data: {action:action,noFactura:noFactura},//datos enviados
        async: true,//retorno de resultado
        success: function (response) {
            if (response == 'error') {//codigo hmtl para mostrar en la vista
                $('.alertAddProduct').html('<p style="color:red;">Error al anular la factura</p>');
            }else{
                $('#row_'+noFactura+' .estado').html('<span class="anulada">Anulada</span>');
                $('#form_anular_factura .btn_ok').remove();
                $('#row_'+noFactura+' .div_factura').html('<button type="button" class="btn_anular inactive"><i class="fa-solid fa-ban"></i></button>');
                $('.alertAddProduct').html('<p>Factura anulada</p>');
                location.reload();
            }
        },
        error: function(error){
            console.log(error);
        }
    });
}
//eliminar pedido de venta
function del_product_detalle (correlativo) {
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var action = 'delProductoDetalle';
    var id_detalle = correlativo;
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        data: {action:action, id_detalle:id_detalle},//datos enviados
        async : true,//retorno de resultado
        success: function (response) {
            if (response != 'error') {
                var info = JSON.parse(response);//codigo hmtl para mostrar en la vista
                $('#detalle_venta').html(info.detalle);
                $('#detalle_totales').html(info.totales);
                //ocultar boton agregar
                $('#add_product_venta').slideUp();
            }else{
                $('#detalle_venta').html('');
                $('#detalle_totales').html('');
            }
            viewProcesar();
        },
        error:function(error){
        }
        
    });
}
//agregar ingrediente al producto en la venta
function updateDT (correlativo, ingrediente){
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var action = 'update_ingredients';
    var id_detalle = correlativo;
    var Dateingrediente = ingrediente;
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async : true,//retorno de resultado
        data: {action:action, id_detalle:id_detalle, Dateingrediente:Dateingrediente},//datos enviados
        success: function (response) {
            if (response != 'error') {
                var info = JSON.parse(response);//codigo hmtl para la vista
                $('#detalle_venta').html(info.detalle);
                $('#detalle_totales').html(info.totales);
                location.reload();
            }else{
                console.log('error');
            }
        },
        error:function(error){
            console.log(error);
        }
        
    });
}
//agregar ingrediente al producto en la venta
function ingreID(input, correlativo){
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var action = 'update_ingredients';
    var idingredient = correlativo;
    var ingrediente = input.value;
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async : true,//retorno de resultado
        data: {action:action, idingredient:idingredient, ingrediente:ingrediente},//datos enviados
        success: function (response) {
            if (response != 'error') {
                location.reload();//refrescar la pagina
            }else{
                console.log('error');
            }
        },
        error:function(error){
            console.log(error);
        }
        
    });

}
//mostrar/Ocultar boton procesar
function viewProcesar () {
    if ($('#detalle_venta tr').length > 0) {
        $('#btn_facturar_venta').show();
    }else{
        $('#btn_facturar_venta').hide();
    }
}
//mostrar todos los productos de ventas
function serchForDetalle (id) {
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var action = 'serchForDetalle';
    var user = id;
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async : true,//retorno de resultado
        data: {action:action, user:user},//datos enviados
        success: function (response) {
            if (response != 'error') {
                var info = JSON.parse(response);//codigo html para mostrar en la vista
                $('#detalle_venta').html(info.detalle);
                $('#detalle_totales').html(info.totales);
                
            }else{
                console.log('no data');
            }
            viewProcesar();
        },
        error:function(error){
        }
        
    });
}
//obtener todas las rutas
function getUrl () {
    var loc = window.location;
    var pathName = loc.pathname.substring(0, loc.pathname.lastIndexOf('/') + 1);
    return loc.href.substring(0, loc.href.length - ((loc.pathname + loc.search + loc.hash).length - pathName.length));
}
//agregar producto
function sendDataProduct () {
    $('.alertAddProduct').html('');
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async:true,//retorno de datos
        data: $('#form_add_product').serialize(),

        success: function(response){
            if (response == 'error') {//codigo html para mostrar en la vista
                $('.alertAddProduct').html('<p style="color:red;">Error Al agregar el producto</p>')
            }else{
                var info = JSON.parse(response);
                $('.row'+info.producto_id+' .celPrecio').html(info.nuevo_precio);
                $('.row'+info.producto_id +' .celExistencia').html(info.nueva_existencia);
                $('#txtCantidad').val('');
                $('#txtPrecio').val('');
                $('.alertAddProduct').html('<p>Producto guardado correctamente </p>')
            }   

        },
        error: function(error){
            console.log(error);
        }
    });
}
//Toast de notificacion para los pedidos
function notify () {
    VanillaToasts.create({
        title:'Nuevo Pedido',
        text: 'Tiene un nuevo pedido',
        type: 'info',
        icon: '../../img/4829979.png',
        timeout: 5000
     });
}
//eliminar producto ex
function delProduct () {
    var pr = $('#producto_id').val();
    $('.alertAddProduct').html('');
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async:true,//retorno de resultado
        data: $('#form_del_product').serialize(),
        success: function(response){
            if (response == 'error') {//codigo html para la vista
                $('.alertAddProduct').html('<p style="color:red;">Error Al eliminar el producto</p>')
            }else{
                $('.row'+pr).remove();
                $('#form_del_product .btn_ok').remove();
                $('.alertAddProduct').html('<p>Producto eliminado correctamente </p>')
            } 
        },
        error: function(error){
            console.log(error);
        }
    });
}
//eliminar producto in
function delProductIn () {
    var pr = $('#producto_id').val();
    $('.alertAddProduct').html('');
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async:true,//retorno de resultado
        data: $('#form_del_product_in').serialize(),
        success: function(response){
            if (response == 'error') {//codigo html para mostrar en la vista
                $('.alertAddProduct').html('<p style="color:red;">Error Al eliminar el producto</p>')
            }else{
                $('.row'+pr).remove();
                $('#form_del_product_in .btn_ok').remove();
                $('.alertAddProduct').html('<p>Producto eliminado correctamente </p>')
            }  

        },
        error: function(error){
            console.log(error);
        }
    });
}
//eliminar usuario
function delUser(){
    var idusuario = $('#usuario_id').val();
    $('.alertAddProduct').html('');
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio   
        type: "POST",//tipo de envio
        async:true,//retorno de resultado
        data: $('#form_del_usuario').serialize(),
        success: function(response){
            if (response == 'error') {//codigo hmtl para mostra en la vista
                $('.alertAddProduct').html('<p style="color:red;">Error Al eliminar el usuario</p>')
            }else{
                $('.row'+idusuario).remove();
                $('#form_del_usuario .btn_ok').remove();
                $('.alertAddProduct').html('<p>Producto eliminado correctamente </p>')
            }  

        },
        error: function(error){
            console.log(error);
        }
    });
}
//eliminar cliente
function delCliente(){
    var cliente_id = $('#cliente_id').val();
    $('.alertAddProduct').html('');
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async:true,//retorno de datos
        data: $('#form_del_cliente').serialize(),
        success: function(response){
            if (response == 'error') {//codigo html para mostrar en la vista
                $('.alertAddProduct').html('<p style="color:red;">Error Al eliminar el cliente</p>')
            }else{
                $('.row'+cliente_id).remove();
                $('#form_del_cliente .btn_ok').remove();
                $('.alertAddProduct').html('<p>Producto eliminado correctamente </p>')
            }  

        },
        error: function(error){
            console.log(error);
        }
    });
}
//eliminar proveedor
function delProveedor(){
    var proveedor_id = $('#proveedor_id').val();
    $('.alertAddProduct').html('');
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async:true,//retorno de datos
        data: $('#form_del_proveedor').serialize(),

        success: function(response){
            //console.log(response);
            if (response == 'error') {//codigo html para mostrar en la vista
                $('.alertAddProduct').html('<p style="color:red;">Error Al eliminar el proveedor</p>')
            }else{
                $('.row'+proveedor_id).remove();
                $('#form_del_proveedor .btn_ok').remove();
                $('.alertAddProduct').html('<p>Producto eliminado correctamente </p>')
            }  

        },
        error: function(error){
            console.log(error);
        }
    });
}
//ocultar el modal
function closeModal () {
    $('.alertAddProduct').html('');
    $('#txtCantidad').val('');
    $('#txtPrecio').val('');
    $('.modal').fadeOut();
}
//ocultar modal de productos internos
function closeModalI () {
    $('#txtCantidad').val('');
    $('#txtPrecio').val('');
    $('.modal_In').fadeOut();
}
//nav efecto
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}
//mostrar factura
function facturaTxt(idcliente,nofactura){
    // definimos la anchura y altura de la ventana
    var altura=680;
    var anchura=630;
    
    // calculamos la posicion x e y para centrar la ventana
    var y=parseInt((window.screen.height/2)-(altura/2));
    var x=parseInt((window.screen.width/2)-(anchura/2));
    $url1 ='../../resources/facturaPDF/index.php?idcliente='+idcliente+'&factura='+nofactura;
    
    var ventana1;
    ventana1=window.open($url1,target='blank','width='+anchura+',height='+altura+',top='+y+',left='+x+',toolbar=no,location=no,status=no,menubar=no,scrollbars=no,directories=no,resizable=no');

}
//actulizar la cantidad
function date_cantidad(input, correlativo){
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var action = 'cantidad';
    var cantVal = input.value;
    var correlativo = correlativo;
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async : true,//retorno de resultado
        data: {action:action, cantVal:cantVal, correlativo:correlativo},//datos enviados
        success: function (response) {
            if (response != 'error') {
                location.reload();
            }else{
                console.log('no data');
            }
            viewProcesar();
        },
        error:function(error){
            console.log(error);
        }
        
    });
}
//actualizar extras
function date_extras(input, correlativo){
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var action = 'valExtras';
    var extrasVal = input.value;
    var correlativo = correlativo;
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async : true,//retorno de resultado
        data: {action:action, extrasVal:extrasVal, correlativo:correlativo},//datos enviados
        success: function (response) {
            if (response != 'error') {
                location.reload();
            }else{
                console.log('no data');
            }
            viewProcesar();
        },
        error:function(error){
            console.log(error);
        }
        
    });
}
//funcion para llevar producto
function date_LlevarUnitario(input, correlativo){
    /**
     * variables en donde se guardaran los valor obtenidos
     */
    var action = 'llevarUnitario';
    var correlativo = correlativo;
    var valor = input.value;
    /**
     * ajax nos permite enviar datos a un lugar determinado
     */
    $.ajax({
        url: "../../ajax.php",//direccion o ruta de envio
        type: "POST",//tipo de envio
        async : true,//retorno de resultado
        data: {action:action, correlativo:correlativo, valor:valor},//datos enviados
        success: function (response) {
            if (response != 'error') {
                location.reload();
            }else{
                console.log('no data');
            }
            viewProcesar();
        },
        error:function(error){
            console.log(error);
        }
        
    });
}

