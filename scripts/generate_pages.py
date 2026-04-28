#!/usr/bin/env python3
import yaml, os, itertools

with open('_data/tools.yml') as f:
    tools = yaml.safe_load(f)
with open('_data/industries.yml') as f:
    industries = yaml.safe_load(f)

template_en = """---
layout: programmatic
lang: en
title: "{tool_name} for {industry_name}"
tool: {tool_id}
industry: {industry_id}
schema_type: "HowTo"
steps:
  - name:
      en: "Step 1: Understand the basics"
      es: "Paso 1: Comprender los conceptos básicos"
    text:
      en: "Learn what {tool_name} offers and how it applies to {industry_name}."
      es: "Aprende qué ofrece {tool_name} y cómo se aplica a {industry_name}."
  - name:
      en: "Step 2: Set up your workflow"
      es: "Paso 2: Configura tu flujo de trabajo"
    text:
      en: "Integrate {tool_name} into your daily {industry_name} tasks using our guide."
      es: "Integra {tool_name} en tus tareas diarias de {industry_name} con nuestra guía."
body:
  en: "Discover how {tool_name} transforms {industry_name} operations. This page is automatically generated from our structured data engine."
  es: "Descubre cómo {tool_name} transforma las operaciones de {industry_name}. Esta página es generada automáticamente por nuestro motor de datos estructurados."
---
"""

template_es = """---
layout: programmatic
lang: es
title: "{tool_name_es} para {industry_name_es}"
tool: {tool_id}
industry: {industry_id}
schema_type: "HowTo"
steps:
  - name:
      en: "Step 1: Understand the basics"
      es: "Paso 1: Comprender los conceptos básicos"
    text:
      en: "Learn what {tool_name} offers and how it applies to {industry_name}."
      es: "Aprende qué ofrece {tool_name_es} y cómo se aplica a {industry_name_es}."
  - name:
      en: "Step 2: Set up your workflow"
      es: "Paso 2: Configura tu flujo de trabajo"
    text:
      en: "Integrate {tool_name} into your daily {industry_name} tasks using our guide."
      es: "Integra {tool_name_es} en tus tareas diarias de {industry_name_es} con nuestra guía."
body:
  en: "Discover how {tool_name} transforms {industry_name} operations. This page is automatically generated from our structured data engine."
  es: "Descubre cómo {tool_name_es} transforma las operaciones de {industry_name_es}. Esta página es generada automáticamente por nuestro motor de datos estructurados."
---
"""

for tool in tools:
    for ind in industries:
        filename_en = f"{tool['id']}-{ind['slug']['en']}.html"
        filename_es = f"{tool['id']}-{ind['slug']['es']}.html"
        # English page
        with open(f'en/{filename_en}', 'w') as f:
            f.write(template_en.format(
                tool_name = tool['name']['en'],
                industry_name = ind['name']['en'],
                tool_id = tool['id'],
                industry_id = ind['id']))
        # Spanish page
        with open(f'es/{filename_es}', 'w') as f:
            f.write(template_es.format(
                tool_name = tool['name']['en'],   # keep English id reference
                tool_name_es = tool['name']['es'],
                industry_name = ind['name']['en'],
                industry_name_es = ind['name']['es'],
                tool_id = tool['id'],
                industry_id = ind['id']))
    print(f"Generated {len(industries)} pages for {tool['name']['en']}")
print("Done. Commit the newly created pages to enable pSEO.")
