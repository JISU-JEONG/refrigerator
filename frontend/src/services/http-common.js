import axios from "axios";

export default axios.create({
  baseURL: "i02b102.p.ssafy.io",
  headers: {
    "Content-type": "application/json"
  }
});
