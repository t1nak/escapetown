$(document).ready(function(){
    $('#print-pdf').on('click', function(event) {
        event.preventDefault();

        var selectedItems = [];
        $('input[name="selected_items"]:checked').each(function() {
            selectedItems.push($(this).val());
        });

        if (selectedItems.length === 0) {
            alert("Please select at least one item.");
            return;
        }

        var url = $("#favorites-form").attr('action');
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            type: "POST",
            url: url,
            data: {
                'selected_items': selectedItems,
                'csrfmiddlewaretoken': csrfToken,
            },
            success: function(response) {
                window.location.href = response.download_url;
            },
            error: function(xhr, status, error) {
                console.log("AJAX Error: ", error);
            }
        });
    });
});
