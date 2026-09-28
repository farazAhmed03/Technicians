from pathlib import Path
p=Path('/home/ubuntu/labrkp-workforce/server/marketplaceApi.ts')
s=p.read_text()
old='''      for (const field of ["profilePhoto", "diplomaProof", "skillProof"]) {
        const file = req.body[field];
        if (file?.data) {
          const content = String(file.data).split(",").pop() || "";
          const uploaded = await storagePut(`worker-applications/${String(req.body.email).replace(/[^a-z0-9]/gi, "-")}/${field}-${Date.now()}-${file.name || "proof"}`, Buffer.from(content, "base64"), file.type || "application/octet-stream");
          documents[field] = { ...uploaded, fileName: file.name || field, contentType: file.type || "application/octet-stream" };
        }
      }'''
new='''      for (const field of ["profilePhoto", "diplomaProof", "skillProof"]) {
        const file = req.body[field];
        if (file?.data) {
          const content = String(file.data).split(",").pop() || "";
          try {
            const uploaded = await storagePut(`worker-applications/${String(req.body.email).replace(/[^a-z0-9]/gi, "-")}/${field}-${Date.now()}-${file.name || "proof"}`, Buffer.from(content, "base64"), file.type || "application/octet-stream");
            documents[field] = { ...uploaded, fileName: file.name || field, contentType: file.type || "application/octet-stream" };
          } catch (uploadError) {
            if (process.env.NODE_ENV === "development") {
              documents[field] = { key: `local-${field}`, url: String(file.data), fileName: file.name || field, contentType: file.type || "application/octet-stream" };
            } else throw uploadError;
          }
        }
      }'''
if old not in s: raise SystemExit('upload block missing')
s=s.replace(old,new,1)
p.write_text(s)

p=Path('/home/ubuntu/labrkp-workforce/client/src/pages/WorkerSignup.tsx')
s=p.read_text()
s=s.replace('''    } catch { setError("Application saved for review. Connect MongoDB to persist it online."); setSubmitted(true); }''','''    } catch (submitError) { setError(submitError instanceof Error ? submitError.message : "Application could not be submitted. Please try again."); }''',1)
p.write_text(s)
