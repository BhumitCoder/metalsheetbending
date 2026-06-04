import os

bt = chr(96)

old_nav = (
    "export function createSiteNavigationJsonLd(): SchemaObject {\n"
    "  return {\n"
    "    \"@context\": \"https://schema.org\",\n"
    "    \"@type\": \"ItemList\",\n"
    "    name: \"Primary Site Navigation\",\n"
    "    itemListElement: [\n"
    "      { name: \"Home\", path: \"/\" },\n"
    "      { name: \"About\", path: \"/about\" },\n"
    "      { name: \"Services\", path: \"/services\" },\n"
    "      { name: \"Products\", path: \"/products\" },\n"
    "      { name: \"Sectors\", path: \"/sectors\" },\n"
    "      { name: \"Blog\", path: \"/blog\" },\n"
    "      { name: \"Contact\", path: \"/contact\" },\n"
    "    ].map((item, index) => ({\n"
    "      \"@type\": \"SiteNavigationElement\",\n"
    "      position: index + 1,\n"
    "      name: item.name,\n"
    "      url: absoluteUrl(item.path),\n"
    "    })),\n"
    "  };\n"
    "}"
)

new_nav = (
    "export function createSiteNavigationJsonLd(): SchemaObject {\n"
    "  const navItems = [\n"
    "    {\n"
    "      name: \"Home\",\n"
    "      path: \"/\",\n"
    "      description: \"Overview of Balaji Engineering Works \u2014 sheet metal fabrication, CNC laser cutting, and industrial products in Surat\",\n"
    "    },\n"
    "    {\n"
    "      name: \"About\",\n"
    "      path: \"/about\",\n"
    "      description: \"Company history, manufacturing capabilities, equipment, and industrial profile of Balaji Engineering Works\",\n"
    "    },\n"
    "    {\n"
    "      name: \"Services\",\n"
    "      path: \"/services\",\n"
    "      description: \"CNC laser cutting, CNC plasma cutting, CNC press brake bending, plate rolling, and sheet metal fabrication services in Surat\",\n"
    "    },\n"
    "    {\n"
    "      name: \"Products\",\n"
    "      path: \"/products\",\n"
    "      description: \"Industrial steel products \u2014 MS base plates, foundation bolts, C/Z purlins, perforated sheets, steel pallets manufactured in Surat\",\n"
    "    },\n"
    "    {\n"
    "      name: \"Sectors\",\n"
    "      path: \"/sectors\",\n"
    "      description: \"Industries served by Balaji Engineering Works \u2014 construction, chemical, pharmaceutical, automotive, power, infrastructure\",\n"
    "    },\n"
    "    {\n"
    "      name: \"Gallery\",\n"
    "      path: \"/gallery\",\n"
    "      description: \"Photo gallery of fabrication work, CNC cutting, bending, welding, and finished products from Balaji Engineering Works\",\n"
    "    },\n"
    "    {\n"
    "      name: \"Blog\",\n"
    "      path: \"/blog\",\n"
    "      description: \"Technical guides and industrial manufacturing articles on sheet metal fabrication, laser cutting, and steel bending\",\n"
    "    },\n"
    "    {\n"
    "      name: \"Contact\",\n"
    "      path: \"/contact\",\n"
    "      description: \"Request a quote or contact Balaji Engineering Works in Surat \u2014 phone, email, and address\",\n"
    "    },\n"
    "  ];\n"
    "\n"
    "  return {\n"
    "    \"@context\": \"https://schema.org\",\n"
    "    \"@type\": \"ItemList\",\n"
    + "    \"@id\": " + bt + "${siteConfig.url}#site-navigation" + bt + ",\n"
    "    name: \"Primary Site Navigation\",\n"
    "    itemListElement: navItems.map((item, index) => ({\n"
    "      \"@type\": \"SiteNavigationElement\",\n"
    + "      \"@id\": " + bt + "${absoluteUrl(item.path)}#nav-item" + bt + ",\n"
    "      position: index + 1,\n"
    "      name: item.name,\n"
    "      description: item.description,\n"
    "      url: absoluteUrl(item.path),\n"
    "    })),\n"
    "  };\n"
    "}"
)

old_breadcrumb = (
    "export function createBreadcrumbJsonLd(items: BreadcrumbItem[]): SchemaObject {\n"
    "  return {\n"
    "    \"@context\": \"https://schema.org\",\n"
    "    \"@type\": \"BreadcrumbList\",\n"
    "    itemListElement: items.map((item, index) => ({\n"
    "      \"@type\": \"ListItem\",\n"
    "      position: index + 1,\n"
    "      name: item.name,\n"
    "      item: absoluteUrl(item.path),\n"
    "    })),\n"
    "  };\n"
    "}"
)

new_breadcrumb = (
    "export function createBreadcrumbJsonLd(items: BreadcrumbItem[]): SchemaObject {\n"
    "  const lastItem = items[items.length - 1];\n"
    "  return {\n"
    "    \"@context\": \"https://schema.org\",\n"
    "    \"@type\": \"BreadcrumbList\",\n"
    + "    \"@id\": lastItem ? " + bt + "${absoluteUrl(lastItem.path)}#breadcrumb" + bt + " : " + bt + "${siteConfig.url}#breadcrumb" + bt + ",\n"
    "    itemListElement: items.map((item, index) => ({\n"
    "      \"@type\": \"ListItem\",\n"
    "      position: index + 1,\n"
    "      name: item.name,\n"
    "      item: absoluteUrl(item.path),\n"
    "    })),\n"
    "  };\n"
    "}"
)

old_employees_end = (
    "    knowsAbout: siteConfig.industries,\n"
    "    numberOfEmployees: {\n"
    "      \"@type\": \"QuantitativeValue\",\n"
    "      value: 50,\n"
    "    },\n"
    "  };\n"
    "}\n"
    "\n"
    "export function createOfferCatalogJsonLd"
)

new_employees_end = (
    "    knowsAbout: siteConfig.industries,\n"
    "    numberOfEmployees: {\n"
    "      \"@type\": \"QuantitativeValue\",\n"
    "      value: 50,\n"
    "    },\n"
    "    potentialAction: [\n"
    "      {\n"
    "        \"@type\": \"ReserveAction\",\n"
    "        name: \"Request a Quote\",\n"
    "        target: {\n"
    "          \"@type\": \"EntryPoint\",\n"
    + "          urlTemplate: " + bt + "${siteConfig.url}/contact" + bt + ",\n"
    "          actionPlatform: [\n"
    "            \"http://schema.org/DesktopWebPlatform\",\n"
    "            \"http://schema.org/MobileWebPlatform\",\n"
    "          ],\n"
    "        },\n"
    "      },\n"
    "    ],\n"
    "  };\n"
    "}\n"
    "\n"
    "export function createOfferCatalogJsonLd"
)

projects = [
    r"C:\Users\STAFF1\Downloads\cncplatebending",
    r"C:\Users\STAFF1\Downloads\sheetmetalbendingworks",
    r"C:\Users\STAFF1\Downloads\Balaji-Dynamic-Site",
]

for project in projects:
    path = os.path.join(project, r"src\lib\seo.ts")
    with open(path, encoding="utf-8") as f:
        content = f.read()
    changed = False
    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        changed = True
        print("  Nav updated: " + project)
    else:
        print("  Nav NOT FOUND in: " + project)
    if old_breadcrumb in content:
        content = content.replace(old_breadcrumb, new_breadcrumb)
        changed = True
        print("  Breadcrumb updated: " + project)
    else:
        print("  Breadcrumb NOT FOUND in: " + project)
    if old_employees_end in content:
        content = content.replace(old_employees_end, new_employees_end)
        changed = True
        print("  potentialAction updated: " + project)
    else:
        print("  potentialAction NOT FOUND in: " + project)
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("SAVED: " + path)
    else:
        print("NO CHANGES: " + path)

print("Done!")
