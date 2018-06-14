$.ajax({
    type: "GET",
    url: "/products/get-place-orders/",
    success : function(response) {
        $.each( response.orders, function( i, val ) {

            let row = "<tr> \
                <td>"+val.id+"</td>\
                <td>"+val.symbol+"</td>\
                <td>"+val.description+"</td>\
                <td>"+val.unit+"</td>\
                <td>"+val.quantity+"</td>\
                <td>"+val.created_date+"</td>\
              </tr>"
            $("table tbody").append(row)
        });
    }
});