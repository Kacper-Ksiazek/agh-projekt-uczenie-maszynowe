<script lang="ts">
import Input from "../ui/input/input.svelte";
import Label from "../ui/label/label.svelte";

import * as Card from "$lib/components/ui/card";

import Progress from "../ui/progress/progress.svelte";
import Button from "../ui/button/button.svelte";
import Step_1 from "./steps/step-1.svelte";

let currentStep = $state<"STEP_1" | "STEP_2" | "STEP_3" | "STEP_4">("STEP_1");

let isFirstStep = $derived<boolean>(currentStep === "STEP_1");
let isLastStep = $derived<boolean>(currentStep === "STEP_4");

let progressValue = $derived.by<number>(() => {
  switch (currentStep) {
    case "STEP_1":
      return 0;
    case "STEP_2":
      return 25;
    case "STEP_3":
      return 50;
    case "STEP_4":
      return 75;
    default:
      return 0;
  }
});

let cardHeader = $derived.by<string>(() => {
  switch (currentStep) {
    case "STEP_1":
      return "Krok 1. Informacje ogólne";
    case "STEP_2":
      return "Krok 2. Preferencje";
    case "STEP_3":
      return "Krok 3. Okres diety";
    case "STEP_4":
      return "Krok 4. Podsumowanie";
    default:
      return "";
  }
});

function nextStep() {
  if (currentStep === "STEP_1") {
    currentStep = "STEP_2";
  } else if (currentStep === "STEP_2") {
    currentStep = "STEP_3";
  } else if (currentStep === "STEP_3") {
    currentStep = "STEP_4";
  }
}

function prevStep() {
  if (currentStep === "STEP_2") {
    currentStep = "STEP_1";
  } else if (currentStep === "STEP_3") {
    currentStep = "STEP_2";
  } else if (currentStep === "STEP_4") {
    currentStep = "STEP_3";
  }
}
</script>

<Card.Root class="mx-auto w-[800px]">
  <Card.Header>
    <Progress value={progressValue} />

    <Card.Title>{cardHeader}</Card.Title>
  </Card.Header>

  <Card.Content class="flex flex-col gap-2">
    {#if currentStep === "STEP_1"}
      <Step_1 />
    {:else if currentStep === "STEP_2"}
      <!-- <Step_2 /> -->
    {:else if currentStep === "STEP_3"}
      <!-- <Step_3 /> -->
    {/if}
  </Card.Content>

  <Card.Footer class="gap-2">
    <Button variant="outline" disabled={isFirstStep} on:click={prevStep}
      >Cofnij</Button
    >
    <Button on:click={nextStep}>Dalej</Button>
  </Card.Footer>
</Card.Root>
