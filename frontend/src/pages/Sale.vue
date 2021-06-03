<template>
  <div class="h-full flex" style="height: 100vh">
    <div class="flex-grow p-4">
      <Product @basketUpdate="basketUpdate" stock="5" />
    </div>

    <div class="bg-blue-400 w-48 h-full flex flex-col">
      <div class="p-2">
        <div class="bg-white text-2xl rounded-xl">Vending Machine</div>
        <div class="bg-blue-600 h-32 rounded-xl mt-8">
          <div>Order</div>
          <div v-for="detail in state.orderDetail" :key="detail.product_id">{{ detail.name }} : {{ detail.quantity }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Product from "../components/Product.vue";

export default defineComponent({
  name: "Sale",
  components: {
    Product,
  },
  setup: () => {
    const netPrice = ref(0);
    const state = ref({
      orderDetail: [],
    });

    const basketUpdate = async (id, count, name) => {
      // console.log(id, count);
      const product = state.value.orderDetail.find(
        (product) => (product.product_id = id)
      );
      const productIndex = state.value.orderDetail.indexOf(product);

      // Not in basket so add it
      if (productIndex === -1){
        state.value.orderDetail.push({product_id: id, quantity: count, name: name})
        return
      }

      // Quantity = 0 delete from the basket
      if (count === 0 && productIndex >= 0) {
        const removedTheProductArr = state.value.orderDetail.filter(product => product.product_id !== id)
        state.value.orderDetail = removedTheProductArr
        return;
      }

      // Change the number in basket
      state.value.orderDetail[productIndex]['quantity'] = count
    };
    return {
      netPrice,
      state,
      basketUpdate,
    };
  },
});
</script>