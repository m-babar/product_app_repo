
    $.ajax({
        type: "GET",
        url: "/products/get-product-records",
        success : function(response) {
            $.each( response.products_info, function( i, val ) {
                
                let quntity = "<input type='text'  name='' class='update_quntity' value=''>" 

                let row = "<tr class='payload-data-tr'> \
                    <td>"+val.id+"</td>\
                    <td>"+val.symbol+"</td>\
                    <td>"+val.description+"</td>\
                    <td>"+val.unit+"</td>\
                    <td data-id="+val.id+" >"+quntity+"</td>\
                  </tr>"
                $("table tbody.payload-data").append(row)

            });
        }
    });

    $(document).on("focusout", "input.update_quntity", function(){
        let prodcut_id = $(this).closest('td').data('id');
        let quntity = $(this).val();
        if($.isNumeric(quntity)){
            swal({
              title: "Are you sure want to place order? ",
              type: "info",
              showCancelButton: true,
              confirmButtonClass: "btn-info",
              confirmButtonText: "Place order",
              closeOnConfirm: false
            },
            function(){
                $.ajax({
                    type: "POST",
                    url: "/products/update-product-quantity/",
                    data : {'id': prodcut_id, 'quantity' : quntity },
                    success : function(response) {
                        swal("Success!", response.message, "success");
                    },
                    error : function(response){
                        swal("Error!", 'Login required.', "error");
                    }
                })
            });
        }else{
            swal("Warning!", "Enter only digit or may not be blank.", "warning")
        }
    })

    $(document).on('keyup', '#search_input', function(){
        if($(this).val().length >= 2){
            // $(".payload-data tr.payload-data-tr").css('display', 'none');
            // $("table tbody.payload-data tr.search-data-tr").remove()
            $("table tbody.payload-data").empty()
            $.ajax({
                type: "GET",
                url: "/products/search-product/?q="+$(this).val()+"",
                success : function(response) {
                    // $("table tbody.payload-data tr.search-data-tr").remove()
                    $("table tbody.payload-data").empty()
                    $.each( response.products_info, function( i, val ) {
                    let quntity = "<input type='text'  name='' class='update_quntity' value=''>" 

                    let row = "<tr class='search-data-tr'> \
                        <td>"+val.id+"</td>\
                        <td>"+val.symbol+"</td>\
                        <td>"+val.description+"</td>\
                        <td>"+val.unit+"</td>\
                        <td data-id="+val.id+" >"+quntity+"</td>\
                      </tr>"
                    $("table tbody.payload-data").append(row)

                    });
                }
            })
        }else{
            // $(".payload-data tr.payload-data-tr").css('display', 'table-row');
            $("table tbody.payload-data").empty()

            $.ajax({
                type: "GET",
                url: "/products/get-product-records",
                success : function(response) {
                    $.each( response.products_info, function( i, val ) {
                        
                        let quntity = "<input type='text'  name='' class='update_quntity' value=''>" 

                        let row = "<tr class='payload-data-tr'> \
                            <td>"+val.id+"</td>\
                            <td>"+val.symbol+"</td>\
                            <td>"+val.description+"</td>\
                            <td>"+val.unit+"</td>\
                            <td data-id="+val.id+" >"+quntity+"</td>\
                          </tr>"
                        $("table tbody.payload-data").append(row)

                    });
                }
            });

        }
    })
