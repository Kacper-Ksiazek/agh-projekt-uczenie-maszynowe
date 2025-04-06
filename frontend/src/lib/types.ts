export type Gender = "MALE" | "FEMALE";
export type Goal = "WEIGHT_LOSS" | "WEIGHT_MAINTENANCE" | "WEIGHT_GAIN";
export type ActivityLevel = "SEDENTARY" | "LIGHT" | "MODERATE" | "ACTIVE";
export type CookingTimePerDay = "30_MINUTES" | "1_HOUR" | "OVER_1_HOUR";

export type DailySchedule = {
  start: string;
  end: string;
  description: string;
};

export interface DietFormData {
  // Step 1
  age: number;
  height: number;
  weight: number;
  gender: Gender;
  goal: Goal;
  activityLevel: ActivityLevel;
  cookingTime: CookingTimePerDay;

  // Step 2
  allergies: string;
  intolerance: string;
  dislikedFoods: string;
  preferredFoods: string;
  kitchenEquipment: string;

  schedule: Array<DailySchedule>;
}
