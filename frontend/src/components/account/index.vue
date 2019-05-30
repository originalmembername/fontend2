<template>
  <div>
    <h1>Welcome back, {{message.first_name}}</h1>
    <h2>Next class: xx.xx.20xx</h2>
    <h3>Your location: {{message.location}}</h3>
    <h3>Upcoming lessons: {{message.upcoming_lessons}}</h3>
    <h3>Past lessons: {{message.past_lessons}}</h3>
    <h3>
      <a target="_blank" :href="message.protocol_url">Your protocol</a>
    </h3>
    <h3>
      <a target="blank" :href="message.folder_url">Your folder</a>
    </h3>
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
    let setMessage = this.setMessage;
    //Request user data from server
    axios.defaults.headers.common["Authorization"] =
      "Token " + axios.defaults.headers.common["Authorization"];
    axios.get("http://localhost:8000/token_auth/", {}).then(function(resp) {
      setMessage(resp.data);
    });
  }
};
</script>
