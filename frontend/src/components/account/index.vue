<template>
  <div>
    <p>{{message}}</p>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";

export default {
  data() {
    return {
      message: ""
    };
  },

  methods: {
    setMessage(message) {
      this.message = message;
    }
  },

  beforeMount() {
    let setMessage = this.setMessage
    //Request user data from server
    axios.defaults.headers.common["Authorization"] =
      "Token " + axios.defaults.headers.common["Authorization"];
    axios.get("http://localhost:8000/token_auth/", {}).then(function(resp) {
      console.log(resp.data.message);
      setMessage(resp.data.message);
    });
  }
};
</script>
