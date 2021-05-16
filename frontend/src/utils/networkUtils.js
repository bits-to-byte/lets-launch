const axios = require("axios").default;

const BASE_URL = "https://letslaunchapp.azurewebsites.net/";

const axiosInstance = () => {
  let config = { baseURL: BASE_URL };
  const token = localStorage.getItem("token");

  if (token)
    config = { ...config, headers: { Authorization: `Token ${token}` } };

  return axios.create(config);
};

export default axiosInstance;
