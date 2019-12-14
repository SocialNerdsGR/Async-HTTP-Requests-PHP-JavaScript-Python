const axios = require('axios')

const requests = Array(10).fill('http://server:8000');

let startDate = new Date();
let start = startDate.getTime();

axios.all(requests.map(request => axios.get(request)))
  .then(responses => {
    responses.forEach(response => {
      console.log(response.data);
    });
    let endDate = new Date();
    console.log('Time waiting: ' + (endDate.getTime() - start) / 1000 + ' secs');
  });
