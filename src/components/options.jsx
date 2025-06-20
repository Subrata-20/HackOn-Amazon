import { Gift, Leaf, Recycle, Sprout, Package } from "lucide-react";

const packagingOptions = [
  {
    id: "minimal",
    icon: Recycle,
    title: "Minimal Packaging",
    description: "Plastic-free, recyclable paper wrap",
    tip: "Avoids up to 30g of plastic waste",
    price: null,
  },
  {
    id: "gift",
    icon: Gift,
    title: "Gift Packaging",
    description: "Recyclable wrap with message card",
    tip: "Adds delight sustainably 🎁",
    price: "+₹25",
  },
  {
    id: "plantable",
    icon: Sprout,
    title: "Plantable Packaging",
    description: "Seed paper wrap – grows into herbs!",
    tip: "Turns into basil or marigold 🌱",
    price: "+₹40",
  },
  {
    id: "compostable",
    icon: Package,
    title: "Compostable Mailer",
    description: "Biodegradable compost-friendly pouch",
    tip: "Fully decomposes within weeks",
    price: null,
  },
  {
    id: "none",
    icon: Leaf,
    title: "No Extra Packaging",
    description: "No padding unless required",
    tip: "Ships with just labels – zero waste",
    price: null,
  },
];

const Packaging = ({ packagingOption, setPackagingOption }) => {
  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h3 className="text-lg font-semibold text-gray-800 mb-4">Packaging Preferences</h3>
      <p className="text-sm text-gray-500 mb-4">
        Choose how you'd like your order packaged — sustainably, always.
      </p>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {packagingOptions.map((option) => {
          const isSelected = packagingOption === option.id;
          const Icon = option.icon;

          return (
            <div
              key={option.id}
              className={`border rounded-lg p-4 cursor-pointer transition 
                ${isSelected ? "border-green-500 bg-green-50" : "border-gray-200 hover:border-green-300 hover:bg-green-50/40"}`}
              onClick={() => setPackagingOption(option.id)}
            >
              <div className="flex justify-between items-start mb-2">
                <div className="flex items-start">
                  <Icon className={`h-5 w-5 mr-2 ${isSelected ? "text-green-600" : "text-gray-500"}`} />
                  <h4 className="font-medium text-gray-900">{option.title}</h4>
                </div>
                {option.price && (
                  <span className="text-sm font-medium text-green-700 bg-green-100 px-2 py-0.5 rounded-full">
                    {option.price}
                  </span>
                )}
              </div>
              <p className="text-xs text-gray-600">{option.description}</p>
              <p className="text-[11px] text-green-600 italic mt-1">{option.tip}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Packaging;
