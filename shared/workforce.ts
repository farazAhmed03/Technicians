export type VerificationStatus = "Pending" | "Under Review" | "Verified" | "Rejected" | "Suspended";

export const PLATFORM_COMMISSION_RATE = 0.03;

export function calculatePayout(servicePrice: number, commissionRate = PLATFORM_COMMISSION_RATE) {
  const commission = Math.round(servicePrice * commissionRate);
  return {
    servicePrice,
    commission,
    workerEarning: servicePrice - commission,
  };
}

export function isBookableWorker(status: VerificationStatus) {
  return status === "Verified";
}

export function normalizeMarketplaceSearch(value: string) {
  return value.trim().toLocaleLowerCase();
}

export type BookingRequestDetails = {
  fullName: string;
  phone: string;
  email: string;
  date: string;
  time: string;
  location: string;
  consent: boolean;
};

export function isBookingRequestComplete(details: BookingRequestDetails) {
  return Boolean(
    details.fullName.trim() &&
      details.phone.trim() &&
      details.email.trim() &&
      details.date &&
      details.time &&
      details.location.trim() &&
      details.consent,
  );
}
