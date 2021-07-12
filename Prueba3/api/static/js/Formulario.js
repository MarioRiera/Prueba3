$('form').on("submit", function(event){
	event.preventDefault();
	var urlBase = "https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/";
	var marca = $(this).find('input').val();
	var formato = "?format=json";
	var urlCompleta = urlBase+marca+formato;
	console.log(urlCompleta);
	$.ajax({
		url: urlCompleta,
		type: "GET",
		dataType: "json",
		success: function(data)
		{
			$("#resultado").empty();
			//console.log(data);
			$.each(data.Results, function(i, item){
				//console.log(item);
				$("#resultado").append("<tr><td>"+item.Make_ID+"</td><td>"+item.Make_Name+
										"<td>" + item.Model_ID + "</td>"+
										"<td>" + item.Model_Name +"</td></tr");
				
			})
		},
		error: function(xhr, ajaxOptions, thrownError)
		{
			console.log(xhr.status);
			console.log(thrownError);
		}
	});
	/*
	$.get(urlCompleta,
	function(data){
		$.each(data.categories, function(i, item){
			console.log(item);
			$("#resultado").append("<tr><td>"+item.Make_ID+"</td><td>"+item.Make_Name+
									"<tr>"+item.Model_ID+"/td>"+
									"<td>"+item.Model_Name+"</td></tr>");
			
		})
	})
	*/

});
