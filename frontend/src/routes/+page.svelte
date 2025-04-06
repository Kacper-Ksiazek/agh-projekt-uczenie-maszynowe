<script lang="ts">
import AiGeneratedDietDetails from "$lib/components/ai-generated-diet-details.svelte";
import DietForm from "$lib/components/diet-form/diet-form.svelte";
import PendingRequest from "$lib/components/pending-request.svelte";
import { sampleDietPlan } from "$lib/mock";
import { isAIGeneratedDietPlan } from "$lib/type-checkers";
import type { AIGeneratedDietPlan, DietFormData } from "$lib/types";
import { createMutation } from "@tanstack/svelte-query";
import { toast } from "svelte-sonner";

let aiGeneratedDiet = $state<AIGeneratedDietPlan | null>(null);
// let aiGeneratedDiet = $state<AIGeneratedDietPlan | null>(sampleDietPlan);

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
        number_of_meals: data.numberOfMealsPerDay,
      }),
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const json = await response.json();

    if (json.error) {
      throw new Error(json.error);
    }

    const responseBody = json?.response as unknown;

    if (isAIGeneratedDietPlan(responseBody)) {
      aiGeneratedDiet = responseBody;
    } else {
      throw new Error("Invalid response format");
    }
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

{#if aiGeneratedDiet !== null}
  <AiGeneratedDietDetails data={aiGeneratedDiet} />
{:else if $generateMutation.isPending}
  <div class="flex flex-grow items-center justify-center">
    <PendingRequest />
  </div>
{:else}
  <div class="flex flex-grow items-center justify-center">
    <DietForm generateDietUsingAI={generateDietUsingAI} />
  </div>
{/if}
