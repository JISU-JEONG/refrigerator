import axios from "axios";

export default axios.create({
  baseURL: "http://15.164.245.67",
  // baseURL: "http://211.213.225.87:8085/",
  headers: {
    "Content-type": "application/json"
  }
});
