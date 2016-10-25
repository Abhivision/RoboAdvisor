import fetch from 'isomorphic-fetch';

let Utils = {

  httpGet: (url) => {
    return fetch(url)
      .then(response => {

        if (response.status >= 200 && response.status < 300) {
          return response;
        }
        else {
          let error = new Error(response.statusText());
          error.response = response;
          throw error;
        }
      })
      .then(response => response.json());
  },

  formatPrice: (price) => {
    price = parseFloat(price).toFixed(2).split('.');
    price[0] = price[0].toLocaleString();

    return price.join('.');
  }
};


export default Utils;