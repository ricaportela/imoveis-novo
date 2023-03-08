function updateCities(pk, selectedCities) {
  if (pk.length == 0) {
    $("#advertises-form.dynamic-city").html("")
    return
  }
  $.ajax({
    type: "GET",
    url: "/settings/get/cities/" + pk + "/",
    dataType: "json",
    beforeSend: function() {
      $("#advertises-form .dynamic-city").spin()
      $("#advertises-form .dynamic-city").html("")
    },
    success: function(content) {
      var json = $.parseJSON(content.object_list)
      $.each(json, function(index, value) {
        let opt = `<option value="${value.pk}" ${
          selectedCities && selectedCities.indexOf(value.pk) >= 0
            ? "selected"
            : ""
        }>${value.fields.name}</option>`
        $("#advertises-form .dynamic-city").append(opt)
      })
    },
    error: function(errormsg) {
      alert("Ocorreu um erro ao obter as cidades.")
    },
    complete: function() {
      $("#advertises-form .dynamic-city").spin(false)
    }
  })
}

function fillFormOnEdit(state, cities) {
  document.querySelector(
    `select#id_state option[value="${state}"]`
  ).selected = true

  updateCities(state, cities)
}

$(document).ready(function() {
  $("#advertises-form")
    .find(".dynamic-state")
    .change(function() {
      updateCities(this.value)
    })
})
