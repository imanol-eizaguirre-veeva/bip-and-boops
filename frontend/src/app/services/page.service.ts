import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '../../environments/environment';
import { StatResponse } from '../dto/stats.interface';
import { PageView } from '../dto/view.interface';

@Injectable({
  providedIn: 'root',
})
export class PageService {
  constructor(private httpClient: HttpClient) {}

  getPages(): Observable<string[]> {
    return this.httpClient.get<string[]>(`${environment.apiURL}/page`);
  }

  getPageViews(pageID: string): Observable<PageView[]> {
    return this.httpClient.get<PageView[]>(
      `${environment.apiURL}/view/page/${pageID}`
    );
  }

  getActiveUsers(pageID: string): Observable<StatResponse> {
    return this.httpClient.get<StatResponse>(
      `${environment.apiURL}/stats/page/${pageID}/active`
    );
  }
}
