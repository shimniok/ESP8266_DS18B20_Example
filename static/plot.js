const url = "http://localhost:5000/temp";

$.getJSON(url).done((response) => {
  console.log(response);
});
