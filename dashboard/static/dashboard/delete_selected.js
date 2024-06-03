 
    $(document).ready(function(){
        $('#delete-selected').on('click', function() {
            var selectedItems = [];
            $('input[name="selected_items"]:checked').each(function() {
                selectedItems.push($(this).val());
            });

            console.log("Selected items to delete: ", selectedItems);  // Debugging line

            if (selectedItems.length === 0) {
                alert("Please select at least one item to delete.");
                return;
            }

            if (confirm("Are you sure you want to delete the selected items?")) {
                var url = "{% url 'dashboard:delete_selected_favorites' %}";
                var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

                $.ajax({
                    type: "POST",
                    url: url,
                    data: {
                        'selected_items': selectedItems,
                        'csrfmiddlewaretoken': csrfToken,
                    },
                    success: function(response) {
                        if (response.success) {
                            location.reload();
                        } else {
                            alert("There was an error deleting the selected items.");
                        }
                    },
                    error: function(xhr, status, error) {
                        console.log("AJAX Error: ", error);
                    }
                });
            }
        });
    });
 
