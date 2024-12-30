const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczMjgwNjcxOCwianRpIjoiZmRjNDU5M2ItNDVkNS00NGZiLWI2MjMtZTdkY2FhZTI3ODc5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IkhvbGEgbXVuZG8iLCJuYmYiOjE3MzI4MDY3MTgsImNzcmYiOiIwZTBjOGM4Mi0yZDY3LTRjNjUtYTg1ZC00N2QyYmY4N2JjYWYifQ.W4voKxcb4CEt8Faeptqm8aIlMZEBBQHJeuLWyt9SRrU'; // Tu token

// ID del registro que quieres obtener
const id_register = 5; 

// Hacer la solicitud GET a la API, pasando el ID en la URL
fetch(`http://127.0.0.1:5000/api/Aldeas/${id_register}`, {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${token}`, // Añadir el token en el encabezado
  }
})
.then(response => response.json())
.then(data => {
  console.log(data); // Ver los datos que devuelve la API
})
.catch(error => {
  console.error('Error:', error); // Si hay algún error en la solicitud
});
