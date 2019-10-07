console.log("HERE");

$((function(context) {
    
    // utc_epoch comes from index.py

    return function() {
       
        var containers = $('.drug-container');
        
        containers.each(function(i, container) {
           
            var did = $(container).attr('data-drug-id');
           
            $.ajax({
                url: "/catalog/drug.tile/" + did,
            }).done(function(content){
                $(container).html(content);
            });
            console.log(444, did);
        });
        //this is all so we know what image we will need to pull in

    }
    
})(DMP_CONTEXT.get()));
