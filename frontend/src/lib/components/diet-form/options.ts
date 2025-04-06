import type {
  ActivityLevel,
  CookingTimePerDay,
  Gender,
  Goal,
} from "$lib/types";
import type { Selected } from "bits-ui";

export const genderOptions: Selected<Gender>[] = [
  {
    value: "MALE",
    label: "Mężczyzna",
  },
  {
    value: "FEMALE",
    label: "Kobieta",
  },
];

export const activityLevelOptions: Selected<ActivityLevel>[] = [
  {
    value: "SEDENTARY",
    label: "Siedzący tryb życia ( brak aktywności fizycznej )",
  },
  {
    value: "LIGHT",
    label: "Lekka aktywność fizyczna ( 1-3 dni w tygodniu )",
  },
  {
    value: "MODERATE",
    label: "Umiarkowana aktywność fizyczna ( 3-5 dni w tygodniu )",
  },
  {
    value: "ACTIVE",
    label: "Wysoka aktywność fizyczna ( 5-7 dni w tygodniu )",
  },
];

export const goalOptions: Selected<Goal>[] = [
  {
    value: "WEIGHT_LOSS",
    label: "Redukcja",
  },
  {
    value: "WEIGHT_MAINTENANCE",
    label: "Utrzymanie wagi",
  },
  {
    value: "WEIGHT_GAIN",
    label: "Przybranie wagi",
  },
];

export const cookingTimeOptions: Selected<CookingTimePerDay>[] = [
  {
    value: "30_MINUTES",
    label: "Mniej niż 30 minut",
  },
  {
    value: "1_HOUR",
    label: "30 minut - 1 godzina",
  },
  {
    value: "OVER_1_HOUR",
    label: "Powyżej godziny",
  },
];
