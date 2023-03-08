;(function handlerBannerForm(document, $) {
  const submitButton = document.getElementById("save-banner")
  submitButton.addEventListener("click", function(event) {
    event.preventDefault()
    const form = document.getElementById("banner-form")
    const options = {
      dataType: "json",
      success: data => {
        const bannerSelect = document.getElementById("id_banner")
        const option = document.createElement("option")
        option.appendChild(document.createTextNode(data.title))
        option.value = data.pk
        bannerSelect.appendChild(option)
        bannerSelect.options.selectedIndex = bannerSelect.length - 1
      }
    }
    $(form).ajaxSubmit(options)
    $("#modal-banner-form").modal("hide")
  })
})(window.document, jQuery)
