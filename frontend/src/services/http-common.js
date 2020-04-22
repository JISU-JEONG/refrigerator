import axios from "axios";

export default axios.create({
  baseURL: "http://15.164.245.67:8085/",
  headers: {
    "Content-type": "application/json"
  }
});
