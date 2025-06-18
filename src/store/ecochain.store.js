import { create } from "zustand";
import axiosInstance from "../lib/axios.js";
import toast from "react-hot-toast";

const useEcochainStore = create((set, get) => ({
  product_name: "",
  product_id: "",
  carbon_kg: "",
  issued_at: "",
  certifying_body: "",
  manufacturer: "",
  materials: "",
  category: "",
  block_hash:"",




  submitdata: async (formData) => {
    try {
      console.log("Submitting data:", formData);
      const response = await axiosInstance.post('/submit', formData);
      console.log("Response from server:", response.data);
      toast.success("Data submitted successfully!");
      const {
        product_name,
        product_id,
        block_hash,
        ect_id
      } = response.data[0];

    
      const formDataObj = new FormData();
      formDataObj.append('seller_name', "x");// Placeholder for seller name from ecosense store
      formDataObj.append('product_name', product_name);
      formDataObj.append('category', formData.category);
      formDataObj.append('ect_no', ect_id);
      formDataObj.append('hash_no', block_hash);
      formDataObj.append('product_id', product_id);

      get().getproductcertificate(formDataObj); // Call to get product certificate

      console.log(response.data)
      return response.data; // ✅ Return the data for external use

    } catch (error) {
      console.error("Error submitting data:", error);
      toast.error("An error occurred while submitting data.");
    }
  },

  verifyect: async (ectid) => {
    try {
      console.log("Verifying ECT ID:", ectid);
      const response = await axiosInstance.get('/verify', {
        params: { ect_id: ectid }
      });

      if (response.status === 200) {
        toast.success("ECT ID verified successfully!");
        return response.data; // ✅ Return the data for external use
      } else {
        toast.error("Failed to verify ECT ID.");
        return null;
      }
    } catch (error) {
      console.error("Error verifying ECT ID:", error);
      toast.error("An error occurred while verifying ECT ID.");
      return null;
    }
  },


  //testing remaining
  getproductcertificate:async(formData) => {
    try {
      console.log("Fetching product certificate:", formData);
      const response = await axiosInstance.post('/generate_product_certificate', formData);
      console.log("Response from server:", response.data);
      toast.success("Product certificate downloaded successfully!");
    } catch (error) {
      console.error("Error fetching product certificate:", error);
      toast.error("An error occurred while fetching product certificate.");
    }
  }
  
}));

export default useEcochainStore;
