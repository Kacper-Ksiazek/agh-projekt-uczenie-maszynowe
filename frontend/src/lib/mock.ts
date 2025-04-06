import type { AIGeneratedSingleMeal, AIGeneratedDietPlan } from "./types"; // jeśli interfejsy są w osobnym pliku

export const sampleDietPlan: AIGeneratedDietPlan = [
  // Dzień 1
  [
    {
      name: "Owsianka z bananem i orzechami",
      description: "Pożywne śniadanie na dobry start dnia",
      ingredients: [
        "płatki owsiane",
        "banan",
        "mleko",
        "orzechy włoskie",
        "miód",
      ],
      macros: {
        calories: 420,
        protein: 12,
        carbs: 58,
        fat: 16,
      },
      recipe_in_steps: [
        "Zagotuj mleko w garnku.",
        "Dodaj płatki owsiane i gotuj przez 5 minut.",
        "Pokrój banana i dodaj do owsianki.",
        "Dodaj orzechy i polej miodem.",
      ],
    },
    {
      name: "Kurczak z ryżem i warzywami",
      description: "Zbilansowany lunch z dużą ilością białka",
      ingredients: [
        "pierś z kurczaka",
        "ryż",
        "brokuły",
        "marchew",
        "oliwa",
        "przyprawy",
      ],
      macros: {
        calories: 600,
        protein: 45,
        carbs: 50,
        fat: 20,
      },
      recipe_in_steps: [
        "Ugotuj ryż według instrukcji.",
        "Podsmaż pokrojonego kurczaka z przyprawami.",
        "Dodaj warzywa i duś przez 10 minut.",
        "Podawaj wszystko razem.",
      ],
    },
    {
      name: "Sałatka z tuńczykiem",
      description: "Lekka kolacja bogata w kwasy omega-3",
      ingredients: [
        "tuńczyk w sosie własnym",
        "mix sałat",
        "pomidor",
        "jajko",
        "oliwa z oliwek",
      ],
      macros: {
        calories: 350,
        protein: 30,
        carbs: 10,
        fat: 22,
      },
      recipe_in_steps: [
        "Ugotuj jajko na twardo i pokrój.",
        "Wymieszaj wszystkie składniki w misce.",
        "Skrop oliwą z oliwek i wymieszaj.",
      ],
    },
  ],

  // Dzień 2
  [
    {
      name: "Jajecznica z warzywami",
      description: "Białkowe śniadanie z warzywami",
      ingredients: ["jajka", "papryka", "cebula", "szpinak", "masło"],
      macros: {
        calories: 380,
        protein: 20,
        carbs: 8,
        fat: 28,
      },
      recipe_in_steps: [
        "Podsmaż cebulę i paprykę na maśle.",
        "Dodaj szpinak i smaż chwilę.",
        "Wbij jajka i smaż aż się zetną.",
      ],
    },
    {
      name: "Makaron pełnoziarnisty z indykiem",
      description: "Obiad o wysokiej zawartości białka i błonnika",
      ingredients: [
        "makaron pełnoziarnisty",
        "pierś z indyka",
        "cukinia",
        "sos pomidorowy",
        "czosnek",
      ],
      macros: {
        calories: 620,
        protein: 40,
        carbs: 65,
        fat: 18,
      },
      recipe_in_steps: [
        "Ugotuj makaron.",
        "Podsmaż indyka z czosnkiem i cukinią.",
        "Dodaj sos pomidorowy i duś 5 minut.",
        "Połącz z makaronem i podawaj.",
      ],
    },
    {
      name: "Jogurt z owocami i nasionami chia",
      description: "Lekka i zdrowa kolacja",
      ingredients: [
        "jogurt naturalny",
        "borówki",
        "maliny",
        "nasiona chia",
        "miód",
      ],
      macros: {
        calories: 300,
        protein: 15,
        carbs: 25,
        fat: 12,
      },
      recipe_in_steps: [
        "Wymieszaj jogurt z owocami.",
        "Dodaj nasiona chia i miód.",
        "Odstaw na kilka minut przed jedzeniem.",
      ],
    },
  ],

  // Dzień 3
  [
    {
      name: "Kanapki z awokado i jajkiem",
      description: "Śniadanie bogate w zdrowe tłuszcze",
      ingredients: [
        "chleb pełnoziarnisty",
        "awokado",
        "jajka",
        "rukola",
        "pieprz",
      ],
      macros: {
        calories: 400,
        protein: 18,
        carbs: 30,
        fat: 24,
      },
      recipe_in_steps: [
        "Ugotuj jajka na twardo i pokrój.",
        "Rozgnieć awokado i dopraw.",
        "Posmaruj chleb pastą z awokado.",
        "Dodaj jajka i rukolę.",
      ],
    },
    {
      name: "Gulasz z soczewicy",
      description: "Roślinny obiad z dużą ilością białka i błonnika",
      ingredients: [
        "soczewica",
        "marchew",
        "seler",
        "cebula",
        "przyprawy",
        "oliwa",
      ],
      macros: {
        calories: 550,
        protein: 25,
        carbs: 45,
        fat: 20,
      },
      recipe_in_steps: [
        "Podsmaż warzywa na oliwie.",
        "Dodaj soczewicę i wodę.",
        "Gotuj do miękkości i dopraw.",
      ],
    },
    {
      name: "Zupa krem z dyni",
      description: "Rozgrzewająca zupa na kolację",
      ingredients: [
        "dynia",
        "ziemniak",
        "cebula",
        "czosnek",
        "bulion",
        "śmietanka",
      ],
      macros: {
        calories: 320,
        protein: 8,
        carbs: 35,
        fat: 15,
      },
      recipe_in_steps: [
        "Podsmaż cebulę i czosnek.",
        "Dodaj dynię i ziemniaka, zalej bulionem.",
        "Gotuj aż warzywa zmiękną.",
        "Zblenduj na krem, dodaj śmietankę.",
      ],
    },
  ],
];
