import { describe, expect, it } from "vitest";
import { aggregateRating, commissionFor, hasRequiredWorkerDocuments, isAllowedKpCity, isValidReviewReply, publicWorkerFromApplication, resolveWorkerSkill } from "./marketplaceApi";
import { calculatePayout, isBookableWorker, isBookingRequestComplete, normalizeMarketplaceSearch } from "../shared/workforce";

describe("LABRKP marketplace business rules", () => {
  it("calculates the configured 3% commission and worker earnings", () => {
    expect(calculatePayout(5000)).toEqual({
      servicePrice: 5000,
      commission: 150,
      workerEarning: 4850,
    });
  });

  it("keeps commission configurable for future admin settings", () => {
    expect(calculatePayout(10000, 0.1)).toEqual({
      servicePrice: 10000,
      commission: 1000,
      workerEarning: 9000,
    });
  });

  it("only exposes verified workers as bookable", () => {
    expect(isBookableWorker("Verified")).toBe(true);
    expect(isBookableWorker("Pending")).toBe(false);
    expect(isBookableWorker("Suspended")).toBe(false);
  });

  it("normalizes directory search input", () => {
    expect(normalizeMarketplaceSearch("  Solar Installation ")).toBe("solar installation");
  });

  it("requires customer identity, schedule, location, and contact consent", () => {
    const details = { fullName: "Ali Khan", phone: "03001234567", email: "ali@example.com", date: "2026-09-20", time: "10:30", location: "House 12, Kohat", consent: true };
    expect(isBookingRequestComplete(details)).toBe(true);
    expect(isBookingRequestComplete({ ...details, consent: false })).toBe(false);
    expect(isBookingRequestComplete({ ...details, location: "  " })).toBe(false);
  });

  it("calculates the marketplace commission for a booking", () => {
    expect(commissionFor(5000, 3)).toEqual({ rate: 3, commission: 150 });
  });

  it("accepts only configured KP cities for worker onboarding", () => {
    expect(isAllowedKpCity("Peshawar")).toBe(true);
    expect(isAllowedKpCity("Kohat")).toBe(true);
    expect(isAllowedKpCity("Islamabad")).toBe(false);
  });

  it("keeps a custom service when the worker selects Other", () => {
    expect(resolveWorkerSkill("Other", "Mobile repair")).toBe("Mobile repair");
    expect(resolveWorkerSkill("Electrical", "Mobile repair")).toBe("Electrical");
  });

  it("projects an approved application into a public worker profile", () => {
    const worker = publicWorkerFromApplication({ applicationId: "LAB-1", name: "Approved Worker", skill: "Mobile repair", city: "Peshawar", gender: "Male", experience: "4 years", bio: "Reliable service", reviewedAt: "2026-09-15" });
    expect(worker.verified).toBe(true);
    expect(worker.city).toBe("Peshawar, KPK");
    expect(worker.applicationId).toBe("LAB-1");
  });

  it("aggregates customer ratings and handles workers with no reviews", () => {
    expect(aggregateRating([])).toEqual({ rating: "New", reviews: 0 });
    expect(aggregateRating([{ rating: 5 }, { rating: 4 }, { rating: 5 }])).toEqual({ rating: "4.7", reviews: 3 });
  });

  it("accepts bounded worker replies and rejects empty or oversized text", () => {
    expect(isValidReviewReply("Thanks for your feedback.")).toBe(true);
    expect(isValidReviewReply("   ")).toBe(false);
    expect(isValidReviewReply("x".repeat(1001))).toBe(false);
  });

  it("requires a worker profile photo and diploma, while skill proof stays optional", () => {
    expect(hasRequiredWorkerDocuments({ profilePhoto: { url: "/photo.jpg" }, diplomaProof: { url: "/diploma.pdf" } })).toBe(true);
    expect(hasRequiredWorkerDocuments({ diplomaProof: { url: "/diploma.pdf" } })).toBe(false);
  });
});
