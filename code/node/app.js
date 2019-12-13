const axios = require('axios')

let requests = [];
for (let i = 1; i <= 10; i++) {
    requests.push('http://server:8000')
}

let startDate = new Date();
let start = startDate.getTime();

axios.all(requests.map(request => axios.get(request)))
  .then(axios.spread(function (...responses) {
    responses.forEach(response => {
        console.log(response.data);
    });
    let endDate = new Date();
    console.log((endDate.getTime() - start) / 1000);
  }));
