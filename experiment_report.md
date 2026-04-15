# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-2A202600374  
**Name:** Lại Đức Anh  
**Date:** 15/04/2026
**Email:** laiducanh26112004@gmail.com

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Danh sach san pham hop le gom Laptop, Chair, Phone, Monitor thuoc cac danh muc ro rang nhu electronics, furniture. Gia tri deu hop le va khong co du lieu bat thuong. | 9 | Du lieu da duoc lam sach: loai bo gia tri am, dien category thieu, dam bao tinh nhat quan |
| Garbage Data (`garbage_data.csv`) | Co san pham gia am (Mystery Box), category rong (Phone), du lieu khong dong nhat gay nham lan khi phan tich va dua ra ket qua. | 4 | Ton tai du lieu loi: gia tri am, thieu category, du lieu khong hop le |

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Khi su dung Garbage Data, Agent de bi anh huong boi cac van de chat luong du lieu. Dau tien la gia tri bat thuong (outliers) nhu san pham co gia am (-10), dieu nay khong hop ly trong thuc te va co the lam sai lech cac phep tinh trung binh hoac danh gia gia tri san pham. Thu hai la du lieu thieu (null values), vi du category rong cua san pham Phone, lam Agent khong the phan loai chinh xac. Ngoai ra, su khong dong nhat ve du lieu (inconsistent data) lam giam kha nang hoc va suy luan cua Agent. Tat ca cac van de nay dan den viec Agent dua ra cau tra loi khong chinh xac hoac thieu day du.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** Dong y.  

Chat luong du lieu dong vai tro quan trong hon prompt vi du lieu la nen tang de Agent hoc va suy luan. Du prompt co tot den dau, neu du lieu dau vao bi loi thi ket qua van se khong chinh xac.