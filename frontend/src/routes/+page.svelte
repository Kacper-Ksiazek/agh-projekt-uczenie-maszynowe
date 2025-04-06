<script lang="ts">
import DietForm from "$lib/components/diet-form/diet-form.svelte";
import PendingRequest from "$lib/components/pending-request.svelte";
import type { DietFormData } from "$lib/types";
import { createMutation } from "@tanstack/svelte-query";
import { toast } from "svelte-sonner";

const API_URL = "http://127.0.0.1:5000/generate";

const generateMutation = createMutation({
  mutationFn: async (data: DietFormData) => {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        age: data.age,
        height: data.height,
        weight: data.weight,
        gender: data.gender,
        goal: data.goal,
        activity_level: data.activityLevel,
        cooking_time_per_day: data.cookingTime,
        number_of_days: data.numberOfDays,
        budget: data.budget,
        allergies: data.allergies,
        intolerance: data.intolerance,
        disliked_foods: data.dislikedFoods,
        preferred_foods: data.preferredFoods,
        kitchen_equipment: data.kitchenEquipment,
      }),
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  },
});

async function generateDietUsingAI(data: DietFormData) {
  await $generateMutation.mutateAsync(data, {
    onSuccess: (data) => {
      toast.success("Dieta została wygenerowana pomyślnie!");
    },
    onError: (error) => {
      toast.error("Wystąpił błąd podczas generowania diety.");
    },
  });
}
</script>

{#if $generateMutation.isPending}
  <PendingRequest />
{:else}
  <DietForm generateDietUsingAI={generateDietUsingAI} />
{/if}
