<template>
  <div class="flex-container">
    <div>
      <form @submit.prevent="createShortlink">
        <div class="input-group">
          <input
            v-model="new_value"
            placeholder="Paste a link"
            class="form-control"
          />
          <button type="submit" class="btn btn-dark">Create Shortlink</button>
        </div>
      </form>
      <h1 :style="{ display: shortlink_display }" id="shortlink-text">
        {{ value }}
      </h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "UrlShortener",
  data: () => {
    return {
      value: null,
      new_value: null,
      shortlink_display: "none",
    };
  },
  methods: {
    async createShortlink() {
      if (this.new_value === null) {
        return;
      }
      fetch("http://localhost:8000/", {
        method: "post",
        body: JSON.stringify({
          url: this.new_value,
        }),
        headers: { "Content-type": "application/json" },
      })
        .then((response) => this.displayShortlink(response))
        .catch((err) => console.error(err));
      return;
    },
    async displayShortlink(response) {
      let res = await response.json();
      this.value = res.shortlink;
      this.new_value = "";
      this.shortlink_display = "block";
      console.log(res);
    },
  },
};
</script>