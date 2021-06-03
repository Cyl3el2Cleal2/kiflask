<template>
  <div class="p-4 border-black border-solid rounded-md border-2">
    <div
      class="w-full h-96"
      :style="{
        backgroundImage: 'url(' + img + ')',
        'background-size': 'cover',
      }"
    >
    </div>

    <div class="text-lg to-blue-800 relative mt-1 w-full sm:flex sm:flex-col">
      <h3 class="p-1">{{ name }}</h3>
      <span class="sm:float-left md:absolute left-0 bottom-0">Price: 35</span>
      <div class="flex sm:order-last md:mx-auto justify-center">
        <button
          class="rounded-full w-8 h-8"
          :disabled="count == 0"
          :class="[count == 0 ? 'bg-red-200' : 'bg-red-400']"
          @click="removeFromBasket()"
        >
          -
        </button>
        <span class="inline-block w-8">{{ count }}</span>
        <button
          class="rounded-full w-8 h-8"
          :disabled="count == stock"
          :class="[count == stock ? 'bg-green-200' : 'bg-green-400']"
          @click="addToBasket()"
        >
          +
        </button>
      </div>

      <span class="sm:inline sm:text-center md:absolute right-0 bottom-0 text-right"
        >{{ stock - count }} item left</span
      >
    </div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "Product",
  props: {
    id: {
      type: Number,
      default: 1,
    },
    name: {
      type: String,
      default: "No name",
    },
    stock: {
      type: Number,
    },
    img: {
      type: String,
      default:
        "http://localhost:5000/img/9e866cc9-30fc-4919-8357-051d7beb57a1Screen_Shot_2563-11-10_at_09.56.50.png",
    },
  },
  // emits: ["basketUpdate"],
  setup: (props, { emit }) => {
    const count = ref(0);

    const addToBasket = async () => {
      if (count.value == props.stock) {
        return;
      }
      count.value++;
      emit("basketUpdate", props.id, count.value, props.name);
    };

    const removeFromBasket = async () => {
      if (count.value == 0) {
        return;
      }
      count.value--;
      emit("basketUpdate", props.id, count.value, props.name);
    };

    return { count, addToBasket, removeFromBasket };
  },
});
</script>

<style scoped>
a {
  color: #42b983;
}

label {
  margin: 0 0.5em;
  font-weight: bold;
}

code {
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
}
</style>
