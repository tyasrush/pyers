const cryptoJS = require("crypto-js")
const axios = require("axios")

var nonce = 1000
params = {
    "method": "getInfo",
    "timestamp": Math.round(new Date()),
    "nonce": nonce
}

var hmacCode = cryptoJS.HmacSHA512(decodeURIComponent(params), decodeURIComponent("")).toString()
console.log(hmacCode)

headers = {
    "Key": "",
    "Content-Type": "application/x-www-form-urlencoded",
    "Sign": hmacCode
}

axios.default.post("https://btcapi.net/tapi", params, { headers: headers }).then(result => {
    console.log("results- "+ JSON.stringify(result.headers))
    console.log("data- "+ JSON.stringify(result.data))
}).catch(error => {
    console.log(error)
})

