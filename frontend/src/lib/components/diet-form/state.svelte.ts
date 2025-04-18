import type { DietFormData, Gender } from "$lib/types";

export const dietState = $state<DietFormData>({
  age: 0,
  height: 0,
  weight: 0,

  gender: "MALE",
  goal: "WEIGHT_MAINTENANCE",
  activityLevel: "LIGHT",
  cookingTime: "1_HOUR",

  allergies: "",
  intolerance: "",
  dislikedFoods: "",
  preferredFoods: "",
  kitchenEquipment: "",
  budget: 0,
  numberOfDays: 1,
  numberOfMealsPerDay: 5,
});
